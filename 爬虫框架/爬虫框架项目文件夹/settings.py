# 默认配置
import logging

DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s"
DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"   #默认时间格式
DEFAULT_LOG_FILENAME = "log.lpg"            # 默认日志文件名称



# 设置并发的数量
COCOURRENT_REQUEST = 5

# 管道的配置
PIPELINES = [
    "pipelines.BaiduPipeline",
    # "pipelines.DoubanPipeline",
]


# 爬虫的配置
SPIDERS = [
    "spiders.baidu.BaiduSpider",
    # "spiders.douban.DoubanSpider",
]

# 下载器中间件
DOWNLOADER_MIDDLEWARES = [
    "downloader_middlewares.TestDownloaderMiddleware1"
]

# 爬虫中间件
SPIDER_MIDDLEWAES = [
    "spider_middlewares.TestSpiderMiddleware1"
]