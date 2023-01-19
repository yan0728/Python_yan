import requests
import json
import random
import datetime

time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
time1 = datetime.date.today().strftime('%Y%m%d')
flowNo = 'NO' + time
fileNo = 'FL' + str(random.randint(10000,99999))
filename = fileNo + '_' + time1 + '_' + str(random.randint(10000,99999))

def creatData():
    header = {'Content-Type':'application/json;charset=UTF-8','User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)','Connection':'keep-alive'}
    url = 'https://test-api-yidong.lianjieabs.com/asset/asset_repair/assetRepair'

    data = {
      "channel": "渠道编号",
      "flowNo": flowNo,
      "fileRepairFO": {
       "addr": "yidong/20210512/180000/FL00001_20210512_64846.zip",
       "assets": ["和包贷借款订单号02"],
       "extension": "pdf",
       "fileNo": fileNo,
       "fileSize": 20480,
       "fileType": "00",
       "filename": filename + ".pdf",
       "loanAmountTotal": 30,
       "requestId": ""
     },
     "time": time,
     "version": "1.1.0"
    }

    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("文件名:" + data['fileRepairFO']['filename']) #打印上传文件名称
    print("<<<<<<<请求信息>>>>>>>")
    if r.status_code == 200:
        print(json.dumps(r.json(),sort_keys=True, indent=2,ensure_ascii = False))
    else:
        print(r.text)
    return r.json()

def requestData():
    header = {'Content-Type': 'application/json;charset=UTF-8',
              'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)', 'Connection': 'keep-alive'}
    url = 'https://test-api-yidong.lianjieabs.com/external/resources'

    data = creatData()
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    # 打印的返回值是json格式
    print("<<<<<<<<<<<<<<<<<<推送response>>>>>>>>>>>>>")
    if r.status_code == 200:
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
    else:
        print(r.text)
    return r.json()

requestData()