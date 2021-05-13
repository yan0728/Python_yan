from faker import Faker
import time
import random

time1 = datetime.date.today().strftime('%Y%m%d')

faker = Faker(locale='zh_CN')

addr =  "yidong/"+ "20210512"+"/180000/"+"FL16551_20210512_64846"+".rar"

No = 'NO' + now_str
address1 = faker.name()
print(now_str,No,time1,addr)
import requests
import json
import random
import time

time = time.strftime("%Y%m%d%H%M%S", time.localtime())
flowNo = 'NO' + time
fileNo = 'FL' + str(random.randint(10000,99999))

# fileNo = 'FL' + str(random.randint(10000,99999))
# faker = Faker(locale='zh_CN')
#
#
#
# time = time.strftime("%Y%m%d%H%M%S", time.localtime())
# No = 'NO' + time
# address1 = faker.name()
# print(time,No,fileNo)
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

print(data['fileRepairFO']['filename'])
