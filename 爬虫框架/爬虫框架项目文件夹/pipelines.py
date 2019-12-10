
class BaiduPipeline:
    """ 处理八度数据的管道"""

    def process_item(self,item,spider):
        """
        处理item
        :param item: 爬虫提取的数据
        :param spider: 传递item股过来的爬虫
        :return: item
        """

        if  spider.name == "baidu":
            # 对百度的数据进行处理
            print("百度管道的数据",item.data)
        return item


class DoubanPipeline:
    """处理豆瓣数据的管道"""

    def process_item(self,item,spider):
        """
        处理item
        :param item: 爬虫提取的数据
        :param spider: 传递item股过来的爬虫
        :return: item
        """

        if  spider.name == "douban":
            # 对百度的数据进行处理
            print("douban管道的数据",item.data)
        return item