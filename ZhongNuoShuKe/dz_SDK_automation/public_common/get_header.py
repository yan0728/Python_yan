# -*- coding: utf-8 -*-
"""
@time :    2023/1/19  15:40
@File:     get_header.py
@Software: PyCharm
@Author :  yanxuelei
@Version:  python3.8
"""

import random
import hashlib
import time
from dz_SDK_automation.setting import config
from dz_SDK_automation.public_common import read_excel_data
import json
import requests



ascii_number_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                          "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                          "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                          "5", "6", "7", "8", "9", "0"]

application_id = "qingdao-yeda"
application_key = "AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY"
security_key = "H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW"
request_id = '0d74164194d899502c02c8b94c8405f1'

# 变量
re = read_excel_data.ReadExcel().getExcelData("小额打款")



class Header:

    def __init__(self,method,content_type,request_path,body):
        self.method = method
        self.content_type = content_type
        self.request_path = request_path
        self.body = body


    def timeStamp(self):
        t = time.time()
        timeStamp = int(round(t * 1000))
        # print("timeStamp:" + str(timeStamp))
        return str(timeStamp)



    def contentMD5(self):
        contentMD5 = hashlib.md5(self.body.encode(encoding="utf-8"))
        return contentMD5.hexdigest()  # 返回摘要，作为十六进制数据字符串值

    def getrequestId(self):
        random_list = []
        for i in range(32):
            random_list.append(random.choice(ascii_number_chars))
        # print(''.join(random_list))
        return ''.join(random_list)

    # 创建验签
    def creatSigna(self):
        SPLIT = "::"
        # 非上传文件
        if self.content_type == "application/json;charset=UTF-8":
            str = (application_id
                   + SPLIT + application_key
                   + SPLIT + request_id
                   + SPLIT + self.contentMD5()
                   + SPLIT + self.timeStamp()
                   + SPLIT + self.method
                   + SPLIT + self.request_path
                   + SPLIT + self.content_type
                   + SPLIT + security_key)

        else:
            str = (application_id
                   + SPLIT + application_key
                   + SPLIT + self.getrequestId()
                   + SPLIT + ""
                   + SPLIT + self.timeStamp()
                   + SPLIT + self.method
                   + SPLIT + self.request_path
                   + SPLIT + self.content_type
                   + SPLIT + security_key)
        hl = hashlib.md5()
        hl.update(str.encode(encoding="utf-8"))
        sign = hl.hexdigest()
        return sign

    def creatHeader(self):
        global request_id
        request_id = self.getrequestId()
        if self.content_type == "application/json;charset=UTF-8":
            header = {
                "X-Zn-Open-App-Id": application_id,
                "X-Zn-Open-App-Key": application_key,
                "X-Zn-Content-MD5": self.contentMD5(),
                "Content-Type": get_content_type,
                "X-Zn-Open-Request-Id": request_id,
                "X-Zn-Open-Timestamp": self.timeStamp(),
                "X-Zn-Open-Signature": h.creatSigna()
            }
        else:
            header = {
                "X-Zn-Open-App-Id": application_id,
                "X-Zn-Open-App-Key": application_key,
                "X-Zn-Content-MD5": "",
                "Content-Type": get_content_type,
                "X-Zn-Open-Request-Id": request_id,
                "X-Zn-Open-Timestamp": self.timeStamp(),
                "X-Zn-Open-Signature": h.creatSigna()
            }
        # print(header)
        return header


# 获取excel行数
get_nrows = re[1]
# print(re[0][0])
# 遍历获取每行入参数据
for i in  range(get_nrows-1):
    get_cast_name = re[0][i]["case_name"]
    get_method = re[0][i]["method"]
    get_content_type = re[0][i]["content_type"]
    get_request_path = re[0][i]["request_path"]
    get_body = re[0][i]["body"]

    # 实例化header
    h = Header(get_method, get_content_type, get_request_path, get_body)

    url = config.BAST_URL + get_request_path
    rheader = h.creatHeader()
    r = requests.post(url=url, data=get_body.encode(), headers=rheader)
    print("<<<<<<<<<<<<" + get_cast_name + ">>>>>>>>>>>")
    # 返回值格式化
    print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
    # print(r.text)


# method = "POST"
# content_type = "application/json;charset=UTF-8"
# request_path = "/bank/auth/request"
# body = '{"corporationIdentity": {"businessCode": "91440300MA5F7UJL2H","corporationName":"泓润供应链管理（深圳）有限公司","ownerName": "陈锦青"},"bankAccount": {"bankAccount": "6214830112267878","bankBranch": "招商银行朝阳支行","bankBranchNo": "123456786543"},"notifyUrl": "/xxx/xxx/xxx"}'



