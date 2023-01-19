import requests
import json
import hashlib
import random
import time
from requests_toolbelt.multipart.encoder import MultipartEncoder

applicationId = "qingdao-yeda"
applicationKey = "AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY"
securitykey = "H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW"
requestytpe = "POST"
requestid = "0d74164194d899502c02c8b94c8405f1"
contenttype="application/json;charset=UTF-8"
file = "1"
# 3.1 上传临时文件
# file = "1.pdf"
# content = MultipartEncoder(
#     fields={
#         "file": (file, open(file, "rb"))
#     },
#     boundary="0d74164194d899502c02c8b94c8405f1")
# contenttype = "multipart/form-data;boundary=0d74164194d899502c02c8b94c8405f1"
# requestpath = "/file/temporary"

# 3.4 文件信息
# contenttype = "application/json;charset=UTF-8"
# requestpath = "/file/info/core/voucher-open/certificate/86b168d3-44e1-4661-854b-2acca75eed9c/1672822967682/开具凭证.jpg"
# content = ""

# 4.1发起小额打款认证请求
# requestpath = "/bank/auth/request"
# content = {
# "corporationIdentity": {
# 		"businessCode": "91440300MA5F7UJL2H",
# 		"corporationName": "泓润供应链管理（深圳）有限公司",
# 		"ownerName": "陈锦青"
# 	},
# 	"bankAccount": {
# 		"bankAccount": "6214830112267878",
# 		"bankBranch": "招商银行",
# 		"bankBranchNo": "12346789012"
# 	},
# 	"notifyUrl": ""
# }

# 4.2小额打款验证
# requestpath = "/bank/auth/validate"
# content = {
#  "flowId": "2661028698933169596",
#  "amount": ""
# }

# 4.3 查看进度
# requestpath = "/bank/auth/progress"
# content = {"flowId":"2661041752580296137"}

# 6.1 发送验证码
# requestpath = "/sms/send-code"
# content = '{"minutes":10,' \
#           '"content":"尊敬的用户您好，您正在进行修改个人账号，验证码为【变量】，有效时间15分钟，验证通过即可修改，请勿向他人泄露",' \
#           '"phone":"02810957721"}'
# 6.2 预先验证短信验证码
requestpath = "/sms/validate/beforehand"
content = '{"phone":"02810957721","sequence":"92652883","code":"167916"}'

# 6.3验证短信验证码，并清理key
# requestpath = "/sms/validate"
# content = '{"phone":"02810957721","sequence":"92652883","code":"167916"}'

# 6.4 发送通知
# requestpath = "/sms/notify"
# content = '{"phone":"01810957727",' \
#           '"content":"尊敬的【闫学雷】，【业达保理】添加您为【博弘产融】的管理员，账号:【13810957727】，登录地址：https://【test-yd-operate.lianjieabs】.com；",' \
#           '"params":[1,2,3,4]}'

# 6.5 查询发送历史
# requestpath = "/sms/search"
# content = '{"phone":"02810957721","startTime":2021-01-01 14:00:00,"endTime":2022-01-01 14:00:00}'

class CreatData:

    def __init__(self,applicationId,applicationKey,securitykey,requestytpe,requestid,contenttype,requestpath,content):
        self.applicationId = applicationId
        self.applicationKey = applicationKey
        self.securitykey = securitykey
        self.requestytpe = requestytpe
        self.requestid = requestid
        self.contenttype = contenttype
        self.requestpath = requestpath
        self.content = content


    def contentMD5(self):
        contentMD5 = hashlib.md5(self.content.encode(encoding="utf-8"))
        return contentMD5.hexdigest()  # 返回摘要，作为十六进制数据字符串值

    def timeStamp(self):
        t = time.time()
        timeStamp = int(round(t * 1000))
        # print("timeStamp:" + str(timeStamp))
        return str(timeStamp)

class GetSignaHeader:
    def __init__(self):
        pass

    def getSigna(self):
        cd = CreatData(applicationId,applicationKey,securitykey,requestytpe,requestid,contenttype,requestpath,content)

        SPLIT="::"
        # 上传文件
        if file != "1":
            str = (applicationId + SPLIT + applicationKey + SPLIT + requestid
                   + SPLIT + ""
                   + SPLIT + cd.timeStamp()
                   + SPLIT + requestytpe
                   + SPLIT + requestpath
                   + SPLIT + contenttype
                   + SPLIT + securitykey)
        else:
            str = (applicationId + SPLIT + applicationKey + SPLIT + requestid
                   + SPLIT + cd.contentMD5()
                   + SPLIT + cd.timeStamp()
                   + SPLIT + requestytpe
                   + SPLIT + requestpath
                   + SPLIT + contenttype
                   + SPLIT + securitykey)
        hl = hashlib.md5()
        hl.update(str.encode(encoding="utf-8"))
        # print("signaTure:" + hl.hexdigest())
        return hl.hexdigest()

    def createHeader(self):
        cd = CreatData(applicationId,applicationKey,securitykey,requestytpe,requestid,contenttype,requestpath,content)
        # 上传文件
        if file != "1":
            header = {
                "X-Zn-Open-App-Id": applicationId,
                "X-Zn-Open-App-Key": applicationKey,
                "X-Zn-Content-MD5": "",
                "Content-Type": contenttype,
                "X-Zn-Open-Request-Id": requestid,
                "X-Zn-Open-Timestamp": cd.timeStamp(),
                "X-Zn-Open-Signature": GetSignaHeader.getSigna(1)
            }

        else:
            header = {
                "X-Zn-Open-App-Id": applicationId,
                "X-Zn-Open-App-Key": applicationKey,
                "X-Zn-Content-MD5": cd.contentMD5(),
                "Content-Type": contenttype,
                "X-Zn-Open-Request-Id": requestid,
                "X-Zn-Open-Timestamp": cd.timeStamp(),
                "X-Zn-Open-Signature": GetSignaHeader.getSigna(1)
            }
        print()
        print("<<<<<<<<<<header>>>>>>>>>>")
        print(header)
        print('X-Zn-Open-App-Id:', header['X-Zn-Open-App-Id'])
        print('X-Zn-Open-App-Key:', header['X-Zn-Open-App-Key'])
        print('X-Zn-Content-MD5:', header['X-Zn-Content-MD5'])
        print('Content-Type:', header['Content-Type'])
        print('X-Zn-Open-Request-Id:', header['X-Zn-Open-Request-Id'])
        print('X-Zn-Open-Timestamp:', header['X-Zn-Open-Timestamp'])
        print('X-Zn-Open-Signature:',header['X-Zn-Open-Signature'])
        return header

g = GetSignaHeader()
g.createHeader()

url = "http://123.57.27.89" + requestpath
print("请求地址："+url)
print("body：" + str(content))
# r = requests.post(url=url,data=content.encode(),headers=GetSignaHeader.createHeader(1))

# print(json.dumps(content,ensure_ascii=False))
print()
print("<<<<<<<<<<响应数据>>>>>>>>>>")
# 返回值格式化
# print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))
# print(r.text)