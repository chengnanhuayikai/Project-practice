# 管道对象



class Pipeline:

    """完成对管道对象的封装"""

    def process_item(self,item):
        """
        实现对item对象的处理
        :param item:
        :return:
        """
        print("item:",item.data )