
import asyncore
import sys
# 客户端的基本开发使用
# 1.定义类并且继承 asyncore.dispatcher

class SocketClient(asyncore.dispatcher):
    # 2.实现类中的回调代码
    def __init__(self,host,port):
        # 调用父类方法
        asyncore.dispatcher.__init__(self)
        # 创建Socket对象
        self.create_socket()
        # 链接服务器
        address = (host,port)
        self.connect(address)

    #  实现handle_connect回调函数
    def handle_connect(self):
        print("连接成功")
    #  实现writable回调函数  返回为True 表可以向服务器发送数据 触发handle_write
    def writable(self):
        return True
    #  实现handle_write回调函数
    def handle_write(self):
        # 内部实现对服务器发送数据的代码
        # 调用send方法发送数据，参数是字节数据
        self.send("hello world".encode("utf-8"))
    #  实现readble回调函数 返回为True 表可以向服务器接受数据 触发handle_read
    def readable(self):
        return True
    #  实现handle_read回调函数
    def handle_read(self):
        # 主动接受数据，参数是需要接受数据的长度
        result = self.recv(1024)
        print(result )
    #  实现handle_error回调函数
    def handle_error(self):
        # 编写处理错误方法
        t,e,tract = sys.exc_info()
        print(t,e,tract)
        self.close()
    #  实现handle_close回调函数
    def handle_close(self):
        print("连接关闭")
        self.close()



# 3. 创建对象并且执行asyncoer.loop进入运行循环



if __name__ == '__main__':
    client = SocketClient('openbarrage.douyutv.com',8601)

    # 开始启动运行循环
    asyncore.loop(timeout=5 )  # timeout 多长时间触发一次