import time
import hashlib
import json


t = time.time()
# 中诺
appId = "ABS_ZHONGNUO"
appSecret = "bwpxmk82cot79h3j"

# 新希望
# appId = "dev_newhope"
# appSecret = 'A99544F8506C40E2A18FFBB9F49F9CA1'

dataStr = "{\"appId\":\"ABS_ZHONGNUO\",\"appSecret\":\"bwpxmk82cot79h3j\"}"
timestamp = str(int(round(t * 1000)))


str = appId+ "&" + dataStr + "&" +timestamp +"&" + appSecret

print(str)

def MD5():
    m = hashlib.md5()

    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()

    print('MD5加密前为 ：' + str)
    print('MD5加密后为小写 ：' + str_md5)
    return str_md5

    # 另一种写法：b‘’前缀代表的就是bytes
    # str_md5 = hashlib.md5(b str).hexdigest()
    # print('MD5加密后为大写 ：' + str_md5.upper())

def creatData():
    req = {
        "apiType": "ABS_AUTH",
        "appId": appId,
        "dataStr": dataStr,
        "sign": MD5(),
        "timestamp": timestamp
    }
    print("****"*3 + "生成请求输入" + "****"*3 )
    print(json.dumps(req))

creatData()