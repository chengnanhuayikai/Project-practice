# 调度器
from hashlib import sha1
from queue import Queue
import w3lib.url
import six
from scrapy_plus.utils.log import logger
from scrapy_plus.utils.queue import Queue as RedisQueue
from scrapy_plus.conf.settings import SCHEDULER_PERSIST
from scrapy_plus.utils.set import NoramlFilterContainer,RedisFilterContainer





def _to_bytes(string):
    if six.PY2: # 当环境是python2
        if isinstance(string,str):
            return string
        else:
            return string.encode("utf-8")  # unicode类型转化为字节类型
    elif six.PY3: # 当环境是python3
        if isinstance(string,str):
            return string.encode("utf-8")
        else:
            return string

class Scheduler:
    """完成调度器模块的封装   队列先进先出"""
    def __init__(self,collector):
        if not SCHEDULER_PERSIST:
            self.queue = Queue()  # 存储的是带抓取的请求
            # 不使用分布式的时候，使用python的集合存储指纹
            self._filter_container = NoramlFilterContainer()
        else:
            # 当决定要使用分布式的时候，使用redis队列
            self.queue = RedisQueue()
            # 使用分布式的时候，redis集合存储指纹
            self._filter_container = RedisFilterContainer()
        # self._filter_container = set() # 保存指纹的集合
        self.collector = collector
        # self.repeat_request_nums = 0 # 统计重复的数量



    def add_request(self,request):
        """
        实现添加request到队列中
        :param request:
        :return:
        """
        # self._filter_request(request) # 在加入请求队列之前先过滤

        # 判断请求是否进行去重，如果不需要，直接添加到队列
        if  not request.filter:  # 不需要去重
            request.fp = self._gen_fp(request)
            self.queue.put(request)
            logger.info("添加不去重的请求<{} {}>".format(request.method,request.url))
            return

        if self._filter_request(request):
            self.queue.put(request)




    def get_request(self):
        """
        实现获取队列中的request对象
        :param request:
        :return: 请求对象
        """
        try:
            return self.queue.get(block=False)
        except:
            return None

    def _filter_request(self,request):
        """
        实现对请求对象的去重
        :param request: 请求对象
        :return: bool
        """
        # 给request对象添加一个fp属性，保存指纹
        request.fp = self._gen_fp(request)
        if not self._filter_container.exists(request.fp):
            self._filter_container.add_fp(request.fp) # 把request指纹添加到指纹集合中
            return  True
        else:
            logger.info("发现重复的请求：<{} {}>".format(request.method,request.url))
            # self.repeat_request_nums += 1
            self.collector.incr(self.collector.repeat_request_nums_key)

    def _gen_fp(self,request):
        """
        生成request对象的指纹
        :param request: request对象
        :return: 指纹字符串
        """
        # 对url地址，请求体，请求参数，请求方法进行加密，得到指纹
        # 对url地址进行排序
        url = w3lib.url.canonicalize_url(request.url)
        # 请求方法
        method = request.method.upper()
        # 请求参数
        params = request.params if request.params is not None else {}
        params = str(sorted(params.items(),key=lambda x:x[0]))

        # 请求排序
        data = request.data if request.data is not None else {}
        data = str(sorted(data.items(),key=lambda x:x[0]))

        # 使用sha1对数据进行加密
        fp =  sha1()
        # 添加url地址
        fp.update(_to_bytes(url))
        # 添加请求方法
        fp.update(_to_bytes(method))
        # 添加请求参数
        fp.update(_to_bytes(params))
        # 添加请求体
        fp.update(_to_bytes(data))

        return fp.hexdigest()       # 返回16进制字符串