# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        url = 'http://www.baidu.com'
        yield scrapy.Request(url=url,meta={'download_timeout':2},callback=self.parse,dont_filter=True)

    def parse(self, response):
        print('----------->')
        print(response.status)
        print(response.request.headers['User-Agent'])
        print(response.request.meta)
