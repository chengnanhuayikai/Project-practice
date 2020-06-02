from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import base64,rsa
def encrypt_str(data):
    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc+CZK9bBA9IU+gZUOc6FUGu7yO9WpTNB0PzmgFBh96Mg1WrovD1oqZ+eIF4LjvxKXGOdI79JRdve9NPhQo07+uqGQgE4imwNnRx7PFtCRryiIEcUoavuNtuRVoBAm6qdB0SrctgaqGfLgKvZHOnwTjyNqjBUxzMeQlEC2czEMSwIDAQAB"
    rsakey = RSA.import_key(base64.b64decode(public_key))  # 导入读取到的公钥
    cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    cipher_text = base64.b64encode(cipher.encrypt(data.encode(encoding="utf-8")))
    return cipher_text


def encrypt_str_1(data):
    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc+CZK9bBA9IU+gZUOc6FUGu7yO9WpTNB0PzmgFBh96Mg1WrovD1oqZ+eIF4LjvxKXGOdI79JRdve9NPhQo07+uqGQgE4imwNnRx7PFtCRryiIEcUoavuNtuRVoBAm6qdB0SrctgaqGfLgKvZHOnwTjyNqjBUxzMeQlEC2czEMSwIDAQAB"
    print(public_key)
    servertime = "1590240491"
    nonce = "D0QPSI"
    # rsakey = RSA.import_key(base64.b64decode(public_key))  # 导入读取到的公钥
    # cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    # cipher_text = base64.b64encode(cipher.encrypt(data.encode(encoding="utf-8")))
    # return cipher_text\

    rsakey = RSA.import_key(base64.b64decode(public_key))
    cipher = PKCS1_v1_5.new(rsakey,"10001")
    sign = base64.b64encode(cipher.encrypt((servertime + "\t" + nonce + "\n" + data).encode(encoding="utf-8")))
    print(sign)



import rsa
def rsa_encrypt(d_str):
    # 生成公钥和私钥
    pubkey, privkey = rsa.newkeys(1024)
    # 将字符串进行编码
    content = d_str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    print ('加密后', crypto)
    return crypto, privkey

def rsa_decrypt(crypto, privkey):
    # 解密
    content = rsa.decrypt(crypto, privkey)
    # 解码
    content = content.decode('utf-8')
    print ('解密结果', content)


import rsa


def useRsaEn(str):
    rsaPublickey = long(n, 16)  # n为modulus
    # rsaPubkey = "EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443"
    key = rsa.PublicKey(rsaPublickey, "10001")  # 65537 为e，一般等于010001

    # passwd = rsa.encrypt(str, key)
    servertime = "1590240491"
    nonce = "D0QPSI"
    passwd = rsa.decrypt(servertime + "\t" + nonce + "\n" + str,key)
    passwd = binascii.b2a_hex(passwd)
    print(passwd)
    return passwd


useRsaEn('12345566')

import PyV8


def usePyV8(message):
    ctxt = PyV8.JSContext()
    ctxt.__enter__()
    js_file = open('security.js')  # security.js在当前目录下
    js_data = js_file.read()
    js_file.close()
    ctxt.eval(js_data)
    rsaEn = ctxt.locals.rsaEn  # rsaEn 为security.js中的function
    ret = rsaEn(message)  # message为rsaEn函数的入
usePyV8('12345678')



import execjs
def get_rsa_pwd(pwd):
    with open("./common/js/security.js", 'r') as f:
        content = f.read() #读取js文件的全部内容到content变量中
    ctx = execjs.compile(content)
    jscode = 'rsaEn("{0}")'.format(pwd) #js代码赋值
    res = ctx.eval(jscode) #执行js代码
    return res
