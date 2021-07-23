
import hashlib
import requests
import json
import time
import random

# 推资产
var_method1 = 'extend.yidong.asset.create'
# 推合同
var_method2 = 'extend.yidong.contract.create'

time = time.strftime("%Y%m%d%H%M%S", time.localtime())
flowNo = 'NO' + time
fileNo = 'FL' + str(random.randint(10000,99999))
# print("业务编号:" + fileNo)

url_server = 'https://test-api-yidong.lianjieabs.com'
url_local = 'http://192.168.31.106:9012'
server = 1 #1:url_server
# def AES():
#     header = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#               'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)', 'Connection': 'keep-alive'}
#     if server == 1:
#         url = url_server + '/asset/yd-asset/aesEncrypt'
#     else:
#         url = url_local + '/asset/yd-asset/aesEncrypt'
#
#     # 推送合同
#     data = 'text={"addr":"/yidong/20210719/153612/test123.pdf",' \
#            '"assets":[],"extension":".zip",' \
#            '"fileName":"test123.pdf","fileNo":"%s",' \
#            '"fileSize":20480,"fileType":"01","loanAmountTotal":null}' % fileNo
#
#     # r = requests.post(url=url, data=json.dumps(data), headers=header)
#     r = requests.post(url=url, data=data.encode("utf-8"), headers=header)
#     print("<<<<<<<AES返回信息>>>>>>>")
#     if r.status_code == 200:
#         print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
#         a = r.json()
#         return a['data']
#     else:
#         print(r.text)

var_channel = 'test13'
# var_content = AES() #推送合同可以使用
var_content = 'BB844B80F251FB56CA4AE5A68C56AF606340E7F2B174BEC9868E9812087D016359C563662D00ED4939A6DBD91D747FC7314872918D9D182A690E9E75D28825B93D550CCE3042F84614D8FEF045402BDC16773FDB5D25603B7001AF43F1E8C476D2785420517B90830B5BC74E4FE5B7E99ECBBD002CC73074DA35D4BD5D31300A79814C370EDDFEBC4758050543B116EECCE774BAF45969A4A27FF0141D94672FA6521D6D2989609B2C23654FC08C2D8E132E3E2F12DCC544BBB745BCBC86AD089170CF57261ED38AEBCD3570D11B76C8'
var_flowNo = flowNo
var_method = var_method2
var_time = time
var_version = '1.0.1'

def pinChuan():
      chuan = ('IUY9JiCa35ktBHKrJaS3s+Q49GRXtbaW'
            'channel{}'
            'content{}'
            'flowNo{}'
            'method{}'
            'time{}'
            'version{}'
            'IUY9JiCa35ktBHKrJaS3s+Q49GRXtbaW'.format(var_channel,var_content,var_flowNo,var_method,var_time,var_version))
      # print("拼串:" + chuan)
      return chuan

def AddMD5():
      str = pinChuan()
      # 创建md5对象
      m = hashlib.md5()

      # Tips
      # 此处必须encode
      # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
      # 因为python3里默认的str是unicode
      # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
      b = str.encode(encoding='utf-8')
      m.update(b)
      str_md5 = m.hexdigest()

      # print('MD5加密前为 ：' + str)
      # print('MD5加密后为小写 ：' + str_md5)

      # 另一种写法：b‘’前缀代表的就是bytes
      # str_md5 = hashlib.md5(b str).hexdigest()
      print('MD5加密后为大写 ：' + str_md5.upper())
      return str_md5.upper()

def requestData():
      header = {'Content-Type':'application/json;charset=UTF-8',
                'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)','Connection':'keep-alive'}

      if server == 1:
          url = url_server + '/external/resources'
      else:
          url = url_local + '/external/resources'

      data = {
          "flowNo": var_flowNo,
          "content": var_content,
          "time": var_time,
          "method": var_method,
          "channel": var_channel,
          "version": var_version,
          "sign": AddMD5()
      }

      r = requests.post(url=url,data=json.dumps(data) ,headers=header)
      # 打印的返回值是json格式
      print("<<<<<<<推送返回信息>>>>>>>")
      print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))
      print(url)
requestData()