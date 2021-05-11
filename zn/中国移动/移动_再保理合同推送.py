
import hashlib
import requests
import json
import time

# 推资产
var_method1 = 'extend.yidong.asset.create'
# 推合同
var_method2 = 'extend.yidong.contract.create'

time = time.strftime("%Y%m%d%H%M%S", time.localtime())
flowNo = 'NO' + time

var_channel = 'test11'
var_content = 'BB844B80F251FB56CA4AE5A68C56AF60129A12F4A6B6BF722C1238E94AF13B15B8E598F89F4A8E1081841E65013F4144F3566510BF9492311F7C88161668F83F51AF1746D3D695FBF0FDAEDD6BFA375F87966544F556F96D36CBFC1CBB96CFD88928D5C54058D60DED129236E3EDBBAC4E6E20CCFC176B63D1680DFD75F3AFB86901DFB2023D16E0B1DB2BAC2D0383E4DC549596F7C7B32CE3A36C155AE27E734068BCFC3D87C7DE8B14F76E657523209DB6CD0EC74DDCDA2951571CBD0131B70A8C9C3FAC10511E451467A6780F144D'
var_flowNo = flowNo
var_method = var_method2
var_time = time
var_version = '1.0.1'

def pinChuan():
      chuan = ('IUY9JiCa35ktBHKrJaS3s+Q49GRXtbaW'
            'channel{}channel'
            'content{}content'
            'flowNo{}flowNo'
            'method{}method'
            'time{}time'
            'version{}version'
            'IUY9JiCa35ktBHKrJaS3s+Q49GRXtbaW'.format(var_channel,var_content,var_flowNo,var_method,var_time,var_version))
      print(chuan)
      return chuan


def AddMD5():
      str = pinChuan()
      # print("str:" + str)

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

def qq():
      header = {'Content-Type':'application/json;charset=UTF-8',
                'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)','Connection':'keep-alive'}
      url = 'https://test-api-yidong.lianjieabs.com/external/resources'

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
      print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))

qq()