
from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

class BaiduSpider(Spider):


    start_urls = ["http://www.douban.com"]


class DoubanSpiser(Spider):

    start_urls = []

    def start_request(self):  # 发送start_urls中url地址的请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        url_temp = "https://movie.douban.com/top250?start={}&filter="
        for i in [ page*25 for page in range(10)]:
            yield Request(url_temp.format(i),headers=headers)


    def parse(self,response):  # 提取页面的数据
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "Host": "movie.douban.com"
        }

        for li in li_list[0:1]:
            item = {}
            item['movie_name'] = li.xpath('.//div/div[2]/div[1]/a/span[1]/text()')[0]
            item['movie_actor'] = li.xpath('.//div/div[2]/div[2]/p[1]/text()')[0]
            item['detail_url'] = li.xpath('.//div/div[2]/div[1]/a/@href')[0]
            print(item['detail_url'])
            yield Request(item['detail_url'],parse='parse_detail',meta={'item':item},headers=headers)



    def parse_detail(self,response):
        item = response.meta.get('item')
        item['movie_starring'] = response.xpath('//*[@id="info"]/span[10]/text()')
        yield Item(item)
