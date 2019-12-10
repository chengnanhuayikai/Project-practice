# 引擎
import time
from datetime import datetime
from scrapy_plus.conf.settings import ASYNC_TYPE
if ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
elif ASYNC_TYPE == "courtine":
    from gevent.pool import Pool
    from gevent.monkey import patch_all
    patch_all()
else:
    raise Exception("不支持异步方式")
from .downloader import Downloader
from .pipeline import Pipeline
from .scheduler import Scheduler
from .spider import Spider
import importlib
from scrapy_plus.http.request import Request
from scrapy_plus.utils.log import  logger

from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddlewares
from scrapy_plus.middlewares.spider_middlewares import SpiderMiddlewares

from scrapy_plus.conf.settings import SPIDERS,\
    PIPELINES,DOWNLOADER_MIDDLEWARES,SPIDER_MIDDLEWAES,COCOURRENT_REQUEST

from scrapy_plus.utils.status_collector import StatsCollectot

class Engine:
    """完成对引擎模块的封装"""

    def __init__(self):
        """
        实例化其他的组件，在引擎中能够通过调用组件的方法实现功能
        :return:
        """
        self.spiders = self._auto_import_instances(SPIDERS,is_spider=True)       # 字典
        self.collector = StatsCollectot(list(self.spiders.keys()))
        self.downloader = Downloader()
        self.scheduler = Scheduler(self.collector)
        self.pipelines = self._auto_import_instances(PIPELINES)      # 列表
        self.spider_mids = self._auto_import_instances(SPIDER_MIDDLEWAES)  # 列表
        self.downloader_mids = self._auto_import_instances(DOWNLOADER_MIDDLEWARES)  # 列表
        self.total_request_num = 0      # 总的请求数
        self.total_response_num = 0     # 总的响应数
        self.pool = Pool(5)  # 实例化线程池对象
        self.is_runing = False # 判断程序是否结束标志


    def _auto_import_instances(self,path,is_spider=False):
        """
        实现模块的动态导入，传入模块路径列表，返回类的实例
        :param path:
        :return:
        """
        if is_spider:
            instances = {}
        else:
            instances = []
        for p in path:
            module_name = p.rsplit(".",1)[0]  # 获取模块的路径名字
            cls_name = p.rsplit(".",1)[-1]  # 获取类名
            module = importlib.import_module(module_name) # 导入模块
            cls = getattr(module,cls_name)    # 获取module下的类
            if is_spider:
                instances[cls().name] = cls()
            else:
                instances.append(cls())
        return instances


    def start(self):
        """
        提供引擎的启动入口
        :return:
        """
        start_time = datetime.now()
        logger.info("爬虫启动：{}".format(start_time))
        logger.info("爬虫启动的爬虫：{}".format(SPIDERS))
        logger.info("爬虫启动的管道：{}".format(PIPELINES))
        logger.info("爬虫启动的下载器中间件：{}".format(DOWNLOADER_MIDDLEWARES))
        logger.info("爬虫启动的爬虫中间件：{}".format(SPIDER_MIDDLEWAES))
        self.is_runing = True
        self._start_engine()
        end_time = datetime.now()
        logger.info("爬虫结束：{}".format(end_time))
        logger.info("爬虫一共运行：{}秒".format((end_time-start_time).total_seconds()))
        # logger.info("总的请求数量：{}个".format(self.total_request_num))
        logger.info("总的请求数量：{}个".format(self.collector.request_nums))
        # logger.info("总的响应数量：{}个".format(self.total_response_num))
        logger.info("总的响应数量：{}个".format(self.collector.response_nums))
        # logger.info("总的重复数量：{}个".format(self.scheduler.repeat_request_nums))
        logger.info("总的重复数量：{}个".format(self.collector.repeat_request_nums))

        # 清除redis中存状态数量统计的键
        self.collector.clear()

    def _start_request(self):
        """初始化请求，调用爬虫的start_request方法，把所有的请求添加到调度器"""
        def _func(spider_name,spider):
        # 1.  调用爬虫的start_request方法，获取request对象
            # 如果start_request中有while True 会发生阻塞
            for start_request in spider.start_request():
                # 对start_request经过爬虫中间件进行处理
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request)

                # 给初始的请求添加spiders属性
                start_request.spider_name = spider_name

                # 2.  调用调度器的add_request方法，添加request对象到调度器中
                self.scheduler.add_request(start_request)
                # self.total_request_num += 1 # 请求数+1
                # 对redis的请求数量+1
                self.collector.incr(self.collector.request_nums_key)


        for spider_name, spider in self.spiders.items():
            self.pool.apply_async(_func,args=(spider_name,spider),callback=self._callback_start_request_nums())

    def _callback_start_request_nums(self):
        self.collector.incr(self.collector.start_rquest_nums_key)

    def _execute_request_response_item(self):
        """处理单个请求，从调度器取出，发送请求，获取响应，parse函数处理，调度器处理"""

        # 3.  调用调度器的get_request方法，获取request对象
        request = self.scheduler.get_request()

        if request is None: # 判断request是否为None，如果是不做后面的处理
            return
        # resquest对象经过下载器中间的process_request进行处理
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request)

        # 4.  调用下载器的get_response方法，获取响应
        response = self.downloader.get_response(request)
        # 把request的meta属性的值传递给response的meta
        response.meta = request.meta

        # response 对象进过下载器中间件的process_response进行处理
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response)
        #  response 对象经过爬虫中间件的process_response进行处理
        for spider_mid in self.spider_mids:
            response = spider_mid.process_response(response)

        # 根据request的spidr_name属性，获取爬虫实例
        spider = self.spiders[request.spider_name]

        # 获取request对象对应响应的parse方法
        parse = getattr(spider,request.parse)

        # 5.  调用爬虫的parse方法，处理响应
        for result in parse(response):

            # 6.  判断结果的类型，如果是request，重新调用调度器的add_request方法
            if isinstance(result,Request):
                # 在解析函数拿到request对象之后，使用process_request进行处理
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_request(result)

                # 对于新的请求，添加spider_name属性
                result.spider_name = request.spider_name


                self.scheduler.add_request(result)
                # self.total_request_num += 1  # 请求数 +1
                self.collector.incr(self.collector.request_nums_key)

            # 7.  如果不是，调用pipeline的process_item方法处理结果
            else:
                # 遍历所有的pipeline，对item进行处理
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result,spider)

        # self.total_response_num += 1  # 响应数 +1
        self.collector.incr(self.collector.response_nums_key)
    def _callback(self,temp):
        if self.is_runing:
            self.pool.apply_async(self._execute_request_response_item(),callback=self._callback)


    def _start_engine(self):
        """
        具体实现引擎的细节
        :return:
        """

        # # 1.  调用爬虫的start_request方法，获取request对象
        # start_request = self.spider.start_request()
        # # 对start_request经过爬虫中间件进行处理
        # start_request = self.spider_mid.process_request(start_request)
        #
        # # 2.  调用调度器的add_request方法，添加request对象到调度器中
        # self.scheduler.add_request(start_request)
        #
        # # 3.  调用调度器的get_request方法，获取request对象
        # request = self.scheduler.get_request()
        # # resquest对象经过下载器中间的process_request进行处理
        # request = self.downloader_mid.process_request(request)
        #
        # # 4.  调用下载器的get_response方法，获取响应
        # response = self.downloader.get_response(request)
        # # response 对象进过下载器中间件的process_response进行处理
        # response = self.downloader_mid.process_response(response)
        # #  response 对象经过爬虫中间件的process_response进行处理
        # response = self.spider_mid.process_response(response)
        #
        # # 5.  调用爬虫的parse方法，处理响应
        # result = self.spider.parse(response)
        #
        # # 6.  判断结果的类型，如果是request，重新调用调度器的add_request方法
        # if isinstance(result,Request):
        #     self.scheduler.add_request(result)
        # # 7.  如果不是，调用pipeline的process_item方法处理结果
        # else:
        #     self.pipeline.process_item(result)

        self.pool.apply_async(self._start_request()) # 初始化请求
        for i in range(COCOURRENT_REQUEST):
            self.pool.apply_async(self._execute_request_response_item(),callback=self._callback)
        while True:
            time.sleep(0.0001)  #
            # self._execute_request_response_item() # 单个请求

            # 循环结束的条件
            # 总的响应数 + 总的重复数量 == 总的请求数量
            if self.collector.start_rquest_nums == len(self.spiders):    # 不会让主线程太快结束
                if self.collector.response_nums + self.collector.repeat_request_nums >= self.collector.request_nums:
                    self.is_runing = False
                    break