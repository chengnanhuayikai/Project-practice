# 爬虫

from scrapy_plus.http.request import  Request
from scrapy_plus.item import  Item
class Spider:
    """完称对spider的封装"""
    start_urls = []   # 爬虫最开始的url地址

    def start_request(self):
        """
        构造请求对象
        :return:
        """
        for url in self.start_urls:
            yield Request(url)


    def parse(self,response):
        """
        默认处理start_url地址对应的响应
        :param response:
        :return:
        """
        yield Item(response.body)