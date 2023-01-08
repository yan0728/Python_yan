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

# 3.4 文件信息
# contenttype = "application/json;charset=UTF-8"
# requestpath = "/file/info/core/voucher-open/certificate/86b168d3-44e1-4661-854b-2acca75eed9c/1672822967682/开具凭证.jpg"
# content = ""
# file = "1"

# 3.1 上传临时文件
file = "1.pdf"
content = MultipartEncoder(
    fields={
        "file": (file, open(file, "rb"))
    },
    boundary="0d74164194d899502c02c8b94c8405f1")

contenttype = "multipart/form-data;boundary=0d74164194d899502c02c8b94c8405f1"

requestpath = "/file/temporary"

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
        contentMD5 = hashlib.md5(str(self.content).encode(encoding="utf-8"))
        # print("contentMD5:" + contentMD5.hexdigest())
        return contentMD5.hexdigest()  # 返回摘要，作为十六进制数据字符串值

    def timeStamp(self):
        t = time.time()
        timeStamp = int(round(t * 1000))
        print("timeStamp:" + str(timeStamp))
        return str(timeStamp)



class GetSignaHeader:
    def __init__(self):
        pass

    def getSigna(self):
        cd = CreatData(applicationId,applicationKey,securitykey,requestytpe,requestid,contenttype,requestpath,content)

        SPLIT="::"
        if file != 1:
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
        print("signaTure:" + hl.hexdigest())
        return hl.hexdigest()

    def createHeader(self):
        cd = CreatData(applicationId,applicationKey,securitykey,requestytpe,requestid,contenttype,requestpath,content)
        if file == "Y":
            header = {
                "X-Zn-Open-App-Id": applicationId,
                "X-Zn-Open-App-Key": applicationKey,
                "Content-Type": contenttype,
                "X-Zn-Open-Request-Id": requestid,
                "X-Zn-Content-MD5":"",
                "X-Zn-Open-Timestamp": cd.timeStamp(),
                "X-Zn-Open-Signature": GetSignaHeader.getSigna(1)
            }
        else:
            header = {
                "X-Zn-Open-App-Id": applicationId,
                "X-Zn-Open-App-Key": applicationKey,
                "Content-Type": contenttype,
                "X-Zn-Open-Request-Id": requestid,
                "X-Zn-Content-MD5": cd.contentMD5(),
                "X-Zn-Open-Timestamp": cd.timeStamp(),
                "X-Zn-Open-Signature": GetSignaHeader.getSigna(1)
            }
        return header

url = "http://123.57.27.89" + requestpath
print("请求地址："+url)
r = requests.post(url=url,data=content,headers=GetSignaHeader.createHeader(1))
# 返回值格式化
print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))

