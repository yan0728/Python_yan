import requests
import json
import random
import time

time = time.strftime("%Y%m%d%H%M%S", time.localtime())
flowNo = 'NO' + time
fileNo = 'FL' + str(random.randint(10000,99999))

def creatData():
    header = {'Content-Type':'application/json;charset=UTF-8','User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)','Connection':'keep-alive'}
    url = 'https://test-api-yidong.lianjieabs.com/asset/asset_repair/assetRepair'

    data = {
      "channel": "渠道编号",
      "flowNo": flowNo,
      "fileRepairFO": {
       "addr": "yidong/20210511/180000/FL00041_20210203-000907-F.zip",
       "assets": ["HBD003"],
       "extension": "pdf",
       "fileNo": fileNo,
       "fileSize": 20480,
       "fileType": "00",
       "filename": fileNo + "_20210203-000907-F.zip",
       "loanAmountTotal": 30,
       "requestId": ""
     },
     "time": time,
     "version": "1.1.0"
    }

    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("文件名:" + data['fileRepairFO']['filename']) #打印上传文件名称
    print("<<<<<<<请求信息>>>>>>>")
    print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))
    return r.json()

def requestData():
    header = {'Content-Type': 'application/json;charset=UTF-8',
              'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)', 'Connection': 'keep-alive'}
    url = 'https://test-api-yidong.lianjieabs.com/external/resources'

    data = creatData()
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    # 打印的返回值是json格式
    print("<<<<<<<<<<<<<<<<<<推送response>>>>>>>>>>>>>")
    print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))

requestData()