# 默认配置
import logging

DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s"
DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"   #默认时间格式
DEFAULT_LOG_FILENAME = "log.lpg"            # 默认日志文件名称


# 选择线程池的方式  courtine/thread
ASYNC_TYPE = "courtine"

# 设置并发的数量
COCOURRENT_REQUEST = 5


# 设置是否需要持久化 和分布式
SCHEDULER_PERSIST = False

# 管道的配置
PIPELINES = [
    "pipelines.BaiduPipeline",
    "pipelines.DoubanPipeline",
]


# 爬虫的配置
SPIDERS = [
    "spiders.baidu.BaiduSpider",
    "spiders.douban.DoubanSpider",
]

# 下载器中间件
DOWNLOADER_MIDDLEWARES = [

]

# 爬虫中间件
SPIDER_MIDDLEWAES = [

]


# redis队列默认配置
REDIS_QUEUE_NAME = "request_queue"
REDIS_QUEUE_HOST = "localhost"
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 0
# redis指纹集合的位置，存储指纹
REDIS_SET_NAME = "request_queue"
REDIS_SET_HOST = "localhost"
REDIS_SET_PORT = 6379
REDIS_SET_DB = 0