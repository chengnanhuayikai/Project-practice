from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

class BaiduSpider(Spider):

    name = "baidu"

    # start_urls = ["http://www.douban.com"]

    def start_request(self):  # 发送start_urls中url地址的请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        for url in ["http://www.douban.com"] * 3:
            yield Request(url,headers=headers)

    def parse(self,response):
        yield Item(response.body[:10])

