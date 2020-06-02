

import execjs
from js_str import  js_str
def run():
    ctx = execjs.compile(js_str)
    passwd = ctx.call("rsaFun","111111")
    print(passwd)




if __name__ == '__main__':
    run()
