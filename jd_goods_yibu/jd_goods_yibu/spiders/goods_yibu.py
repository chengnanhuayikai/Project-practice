# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from lxml import etree
from fake_useragent import UserAgent
from jd_goods_yibu.items import JdGoodsYibuItem

class GoodsYibuSpider(scrapy.Spider):
    name = 'goods_yibu'
    allowed_domains = ['www.jd.com']
    # start_urls = ['http://www.jd.com/']

    number = 1

    def start_requests(self):

        ua = UserAgent()
        headers = {
            'user-agent': ua.random
        }

        html = '''
            
<a href="//list.jd.com/list.html?cat=6728,6742,13243" target="_blank">减震器</a >
<a href="//list.jd.com/list.html?cat=6728,6742,13295" target="_blank">柴机油/辅助油</a >
<a href="//list.jd.com/list.html?cat=6728,6742,6766" target="_blank">雨刷</a >
<a href="//list.jd.com/list.html?cat=6728,6742,6768" target="_blank">车灯</a >
<a href="//list.jd.com/list.html?cat=6728,6742,9988" target="_blank">后视镜</a >
<a href="//list.jd.com/list.html?cat=6728,6742,9248" target="_blank">轮胎</a >
<a href="//list.jd.com/list.html?cat=6728,6742,11951" target="_blank">轮毂</a >
<a href="//list.jd.com/list.html?cat=6728,6742,11859" target="_blank">刹车片/盘</a >
<a href="//list.jd.com/list.html?cat=6728,6742,6769" target="_blank">维修配件</a >
<a href="//list.jd.com/list.html?cat=6728,6742,9971" target="_blank">蓄电池</a >
<a href="//list.jd.com/list.html?cat=6728,6742,9964" target="_blank">底盘装甲/护板</a >

<a href="//list.jd.com/list.html?cat=6728,6742,6770" target="_blank">贴膜</a >
<a href="//list.jd.com/list.html?cat=6728,6742,6795" target="_blank">汽修工具</a >
<a href="//list.jd.com/list.html?cat=6728,6742,12406" target="_blank">改装配件</a >
<a href="//list.jd.com/list.html?cat=6728,6740,11867" target="_blank">导航仪</a >
<a href="//list.jd.com/list.html?cat=6728,6740,9959" target="_blank">安全预警仪</a >
<a href="//list.jd.com/list.html?cat=6728,6740,6964" target="_blank">行车记录仪</a >
<a href="//list.jd.com/list.html?cat=6728,6740,9961" target="_blank">倒车雷达</a >
<a href="//list.jd.com/list.html?cat=6728,6740,9962" target="_blank">蓝牙设备</a >
<a href="//list.jd.com/list.html?cat=6728,6740,6965" target="_blank">车载影音</a >
<a href="//list.jd.com/list.html?cat=6728,6740,6807" target="_blank">净化器</a >
<a href="//list.jd.com/list.html?cat=6728,6740,6749" target="_blank">电源</a >

            '''
        page_list = []  # [（分类，多少页）]
        url_list =   re.findall('<a href="(.*?)" target="_blank">.*?</a>', html, re.S)
        for url in url_list:
            url = 'https:' + url
            response = requests.get(url=url, headers=headers)
            page_html = etree.HTML(response.text)
            # print(page_html.xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()'))
            try:
                page_number = int(page_html.xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()')[0])  # 共多少页
                page_list.append((url, page_number))
            except :
                pass
        print(page_list)
        for item in page_list:
            for page in range(1, item[1] + 1):
                yield scrapy.Request(url=item[0], callback=self.pase_good, dont_filter=True)

                # break

    def pase_good(self, response):
        # print('------------>',response.headers)
        goods_details_list = re.findall('<div class="p-img" .*?<a target="_blank" href="(.*?)" >', response.text, re.S)
        for good in goods_details_list:
            good_url = "https:" + good
            yield scrapy.Request(url=good_url, callback=self.parse, dont_filter=True)
            # break

    def parse(self, response):
        # print(response.text)
        # html = Selector(text=response.text)
        # print()
        # # response.selector.register_namespace('d', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        # try :
        #     topic_abstract = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]').xpath('string(.)').extract_first().replace(' ','').replace('\n','|')
        #
        #     if '商品名称' in topic_abstract:
        #         pass
        #     else:
        #         topic_abstract = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]').xpath('string(.)').extract_first().replace(' ','').replace('\n','|')
        # except :
        #     topic_abstract = ''

        item = JdGoodsYibuItem()
        try:
            item['topic_title'] = response.xpath('//div[@class="sku-name"]/text()').extract_first().strip()
            # item['topic_abstract'] = topic_abstract # //*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]
            item['topic_cate_level_one'] = response.xpath(
                '//*[@id="crumb-wrap"]/div/div[1]/div[1]/a/text()').extract_first()  # //*[@id="crumb-wrap"]/div/div[1]/div[1]/a
            item['topic_cate_level_two'] = response.xpath(
                '//*[@id="crumb-wrap"]/div/div[1]/div[3]/a/text()').extract_first()
            item['topic_cate_level_three'] = response.xpath(
                '//*[@id="crumb-wrap"]/div/div[1]/div[5]/a/text()').extract_first()
            #
            print('--------------->', self.number)
            print(item['topic_title'])
            # print(item['topic_abstract'])
            print(item['topic_cate_level_one'])
            print(item['topic_cate_level_two'])
            print(item['topic_cate_level_three'])
            self.number += 1
        except Exception as e:
            print('*********************', e)
            item['topic_title'] = None
        yield item

