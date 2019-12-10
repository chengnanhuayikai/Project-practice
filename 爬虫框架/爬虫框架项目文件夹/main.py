from scrapy_plus.core.engine import Engine
from spiders.baidu import BaiduSpider
from spiders.douban import DoubanSpider
from pipelines import BaiduPipeline,DoubanPipeline
from spider_middlewares import TestSpiderMiddleware1,TestSpiderMiddleware2
from downloader_middlewares import TestDownloaderMiddleware1,TestDownloaderMiddleware2
import settings
if __name__ == '__main__':
    # 实例化爬虫
    # baidu = BaiduSpider()
    # douban = DoubanSpider()
    # spiders = {baidu.name:baidu,douban.name:douban}
    # pipelines = [BaiduPipeline(),DoubanPipeline()]
    # spider_mids = [TestSpiderMiddleware1(),TestSpiderMiddleware2()]
    # downloader_mids = [TestDownloaderMiddleware1(),TestDownloaderMiddleware2()]
    engine = Engine()      # 实例化引擎
    engine.start()              # 引擎启动