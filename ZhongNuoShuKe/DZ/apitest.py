import requests
import json
import hashlib
import random
import time
from requests_toolbelt.multipart.encoder import MultipartEncoder

# 3.4 文件信息
# requestpath = "/file/info/core/voucher-open/certificate/86b168d3-44e1-4661-854b-2acca75eed9c/1672822967682/开具凭证.jpg"
# content = ""

# 3.1 上传临时文件
# file = "1.pdf"
# content = MultipartEncoder(
#     fields={
#         "file": (file, open(file, "rb"))
#     },
#     boundary="0d74164194d899502c02c8b94c8405f1")
#
# contenttype = "multipart/form-data;boundary=0d74164194d899502c02c8b94c8405f1"
# requestpath = "/file/temporary"

# 4.1发起小额打款认证请求
requestpath = "/bank/auth/request"
content = {
	"corporationIdentity": {
		"businessCode": "91440300MA5F7UJL2H",
		"corporationName": "泓润供应链管理（深圳）有限公司",
		"ownerName": "陈锦青"
	},
	"bankAccount": {
		"bankAccount": "6214830112267878",
		"bankBranch": "招商银行",
		"bankBranchNo": "12346789012"
	},
	"notifyUrl": ""
}


contenttype = "application/json;charset=UTF-8"
file =1
SPLIT="::"
applicationId = "qingdao-yeda"
applicationKey = "AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY"
securitykey = "H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW"
requestytpe = "POST"
requestid = "0d74164194d899502c02c8b94c8405f1"

def contentMD5():
    contentMD5 = hashlib.md5(str(content).encode(encoding="utf-8"))
    # print("contentMD5:" + contentMD5.hexdigest())
    return contentMD5.hexdigest() #返回摘要，作为十六进制数据字符串值

# def requestId():
#     ranster = random.randint(10000,99999)
#     m = hashlib.md5(str(ranster).encode(encoding="utf-8"))
#     print("X-Zn-Open-Request-Id:" + m.hexdigest())
#     return m.hexdigest()

# 时间戳毫秒级别

def timeStamp():
    t = time.time()
    timeStamp = int(round(t * 1000))
    print("timeStamp:"+ str(timeStamp))
    return str(timeStamp)


def signaTure():
    # 1是非上传文件
    if file == 1:
        str = (applicationId+ SPLIT + applicationKey + SPLIT + requestid
                + SPLIT + contentMD5()
                + SPLIT + timeStamp()
                + SPLIT + requestytpe
                + SPLIT + requestpath
                + SPLIT + contenttype
                + SPLIT + securitykey)
    else:
        str = (applicationId + SPLIT + applicationKey + SPLIT + requestid
               + SPLIT + ""
               + SPLIT + timeStamp()
               + SPLIT + requestytpe
               + SPLIT + requestpath
               + SPLIT + contenttype
               + SPLIT + securitykey)
    hl = hashlib.md5()
    hl.update(str.encode(encoding="utf-8"))
    print("signaTure:" + hl.hexdigest())
    return hl.hexdigest()


def reqApi():
    if file == 1:
        header = {
            "X-Zn-Open-App-Id": applicationId,
            "X-Zn-Open-App-Key":applicationKey ,
            "Content-Type": contenttype,
            "X-Zn-Open-Request-Id": requestid,
            "X-Zn-Content-MD5": contentMD5(),
            "X-Zn-Open-Timestamp": timeStamp(),
            "X-Zn-Open-Signature": signaTure()
        }
    else:
        header = {
            "X-Zn-Open-App-Id": applicationId,
            "X-Zn-Open-App-Key": applicationKey,
            "Content-Type": contenttype,
            "X-Zn-Open-Request-Id": requestid,
            "X-Zn-Content-MD5": "",
            "X-Zn-Open-Timestamp": timeStamp(),
            "X-Zn-Open-Signature": signaTure()
        }

    url = "http://123.57.27.89" + requestpath
    print("请求地址："+url)
    r = requests.post(url=url,data=json.dumps(content) ,headers=header)

    # 返回值格式化
    print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))

reqApi()