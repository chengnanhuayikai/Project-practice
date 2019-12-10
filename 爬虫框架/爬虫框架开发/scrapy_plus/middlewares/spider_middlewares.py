
# 爬虫中间件



class SpiderMiddlewares():


    def process_request(self,request):

        # print("*****爬虫中间件*****")

        return request

    def process_response(self, response):
        # print("*****爬虫中间件*****")

        return response