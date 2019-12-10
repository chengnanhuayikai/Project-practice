# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
import time


class JdGoodsYibuPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '22222',
            db = 'goods',
            charset = 'gbk'
        )
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):


        if item['topic_title'] == '' or item['topic_title'] == None:
            pass
        else:
            sql = 'insert into jd_goods_1(topic_title,topic_cate_level_one,topic_cate_level_two,topic_cate_level_three) values(%s,%s,%s,%s)'
            try:
                self.cursor.execute(sql, (
                item['topic_title'],  item['topic_cate_level_one'], item['topic_cate_level_two'], item['topic_cate_level_three']))
                self.conn.commit()
            except:
                self.conn.rollback()
        return item

    def close_spider(self, spider):
        print('----------- write ok -------------')
        self.cursor.close()
        self.conn.close()

    # def __init__(self):
    #     self.f = open('/Users/songhuan/Documents/jd_fenlei/jd_对讲机.csv','a',encoding='gbk')
    #
    #
    # def process_item(self, item, spider):
    #     if item['topic_title'] == '' or item['topic_title'] == None:
    #         pass
    #     else:
    #         data = item['topic_title'] + ',' + item['topic_abstract'] + ','  + item['topic_cate_level_one'] + ',' + item['topic_cate_level_two'] + ',' + item['topic_cate_level_three'] + '\n'
    #         # print(data)
    #         self.f.write(data)
    #         return item
    #
    # def close_spider(self,spider):
    #     print('----------- write ok -------------')
    #     self.f.close()