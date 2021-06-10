
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
print("业务编号:" + fileNo)

url_server = 'https://test-api-yidong.lianjieabs.com'
url_local = 'http://192.168.31.106:9012'
server = 1 #1:url_server
def AES():
    header = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)', 'Connection': 'keep-alive'}
    if server == 1:
        url = url_server + '/asset/yd-asset/aesEncrypt'
    else:
        url = url_local + '/asset/yd-asset/aesEncrypt'

    # 推送合同
    data = 'text={"addr":"yidong/20210510/180000/移动资料.zip",' \
           '"assets":[],"extension":".zip",' \
           '"fileName":"再保理合同.pdf","fileNo":"%s",' \
           '"fileSize":20480,"fileType":"01","loanAmountTotal":null}' % fileNo

    # r = requests.post(url=url, data=json.dumps(data), headers=header)
    r = requests.post(url=url, data=data.encode("utf-8"), headers=header)
    print("<<<<<<<AES返回信息>>>>>>>")
    if r.status_code == 200:
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
        a = r.json()
        return a['data']
    else:
        print(r.text)

var_channel = 'test13'
# var_content = AES() #推送合同可以使用
var_content = 'CA997606D272F123E8E834C8D045864134FD1720648F552D46A303EC312A8D9A914C795B8092A1AF2B0E525C2703B3004500A42D226CC9B8882CDC53FEADF6101B2B17E2D4AC971D22358D0BFE99E9E0B1C478CB63B46B2D4499D3358EF621AE7AB05450FAF4667356FD05DA5C71AB69A7FF27A7D752742A9383D0F318AF94499B9B885FFFB250677052CFF499876E853F5CF90114E0E810D4F11B94332C09ECCA7E3F34688BC4D130CE0A6CB0D9A8B2DD6BC3F441667EE8A807AA3B98B5F0AE01432170DAB5C4AB6370D20EA2E6BFAFF84ED5E850A1BDEB6915849A714F6539BAE293B25C084C930B7AC1D89A35A64718052CDC8B0F426FB161DEA73040F4A6DFDBE1B6ACA8867A1D692D06799F447B05B8342122AB776E16687A7D55AC2DE76E8CFF72106804719C44BB486134BEAE1739F18C2E7C0F6FC4C201C5739E1B2F7AC30EE26B2BB06A46F431F48FFAA06370B7B0828AB5D67A83FD5C93D83F51847112131BC4EA2350D823EF02B79ABA552D113C1D8CC297515F5EB9A6077272620DDC0CADA470DDC7DC2E9B82FAC4843A105789FE04BE74B680AB8FB14791674F866B0C0C999FEF1FB9CA77F0E01B32F17BB596646C4428909CE308FE1BA50EFC321C2BBE98D37B800CD6D9FC6B38622DEE1030C668C47D7FF00EAA6BAF8FF7BD901BCE7102878A27F39A3864BD3BE43A0F672D530BD693DB8717E4F9036C45AF2BC3A10E4F03CFCACFFAB171F0F0A85EA4189C09FFECF683DD8B69F9E7780AB4D59FBD9CDB8E09DC40CFA825576045F937B5A152D9C233CD11F27ED20E486C4DB472A798DEB17486F99AACBDB270D33DC4B2FAA01006E4EFF85F1F20EA8DC267DC79B65816ABA8FB975A8A148285B2B69D9780C7ECC53E493B4BA446396FAC79EF9FE797AFF52AB318F8A64BAF4FD3BEFD7C5466BB4186A9733AC26B089C592C7CDDFA9493787DBB73D6ED0D4D549480C611B3397918335573C208E687043AB96234857850420C70E81B77596D2CE424556FFDC01B03FF99E065BAD2E0B5606E0F6A28F5419F27661069D6FF825E3CDB0E355F1B448ADC4348C739F7275623465929BFB7AD8CB397FEF9D4B74F63CE2CCF391CAB6E8233381792928127BBBD8590C72CA29D73CE6242825A0F0C4D1967FFBC73405EB3EE65F17B810448F2DD5549FCEB77E6104BFA5DFE5A915916964A140DEC79AB81BD63D9B226B19D50977A598564B2CAF6677682FC8EDF238275A0F21E0F9056F30B436EDBE13A344AAAD0401BABD498A437477CD021065A4C1A15980D006DD725AD728C36A07A6251A9BFE02B1C2FCBB3916BBF8FED6487C84B85050A53153DE7D4CC257C898DAACC6FB40F993E3991341329238435261A3BA3D00770319500DDEC4A61727BE9217F904924E5E8BD00B39964A25569CFC55F79E031533332DAC041F7D645985F743CA322AF1AED85EF3CF36CB1A342121BECDFF4B5BBAD53930C01801D231E69E01B532E51C954022D3D1165CF3922D3F9235D024F487E17AC2F9D10463A4C15C03BBE365729DB9D45411CD4CDE3B05F19004A073BC9272C8E38DA70CA4CDD22579BFC7D3AA3F17EFE78D83B2B76F0F3F782775314CAD21C3B42EDD83C8235D6174E51CA81985AB584C1165C4B3DBE08E3E71682807251D144C4558E947FA92C0D10E465F3A199AEA6382413BBD446039A9F32DCBD3D045DD8493D17FB63C9E428842C1330FC454735880EE3C494F3396A0A381529DAD0C99AFC6951274DB3A267B3E0E779099EADC0E08BB515E6BEAD1F00AFFF88D4F6FC7A6E9218C3AFE365B80F3293871A80C296AEF4702E70A7DE4CDB1659770AF754BED463C4A25C135A31165BF573AD0590114D444332DD18CE17F5B49336B94A8EB2A9633B04426E4693CDE2783F84158E12F685ED2425A57B4B29B7E347717732E8F1C11D6E8A6986BA2C41C7D279945DC0DAE13C3515FFBB00A76B0757A8F2773B69562D7C9E25E4688AC97BD69F391EF72163DD4C4DD1B00261941EF24D464B2C924D189E8EEC9C57E57FC9F97CEAC03AD6E4A30F8C34E90296BA51926DF2DACD4DB2328600D11871CAA14CC5813E1ED3884156345C04AA8A91054A4663B75FAF30E735F1686A32A68D81257373F65E2E083168E3C622ABC970FD75144833029921EDD18C7D76E3E057752DEC3550435DE13156754BAE5DEB24713BA8F16FEDD55317912D9B2519B347A5B92B4D08DCC72C231EFB775E589BCC7E5EA69F15C069DEFF015E2D3AB353D5985F96FE7FAFF8FB447AD1F6DDCE8C5B67550BC1347E84DF11569D34382D020402BDE8F32E7E03AF83D257D03FB4641E41B4C4BD6134BAB3ABE96E1130FA3D7D8B1D9BD3353D8D8B29D4A0D016C5EBCD1FAF4FC9B2048EB81BCEEA87F6C7A1698A44'
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