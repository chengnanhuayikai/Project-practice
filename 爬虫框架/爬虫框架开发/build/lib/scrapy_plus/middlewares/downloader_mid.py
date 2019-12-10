
# 下载器中间件

class DownloaderMid():


    def process_request(self,response):

        print("*****下载器中间件*****")
        return response

    def process_response(self, response):
        print("*****下载器中间件*****")

        return response