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


ascii_number_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                          "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                          "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                          "5", "6", "7", "8", "9", "0"]

application_id = "qingdao-yeda"
application_key = "AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY"
security_key = "H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW"
request_id = '0d74164194d899502c02c8b94c8405f1'
# timeStamp = 1
method = "post"
content_type = "application/json;charset=UTF-8"
request_path = "/sms/validate/beforehand"
body = '{"phone":"02810957721","sequence":"92652883","code":"167916"}'

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
        global request_id
        request_id = self.getrequestId()
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
        print('X-Zn-Open-Signature:', sign)
        # print(str)
        return sign

    def creatHeader(self):

        if self.content_type == "application/json;charset=UTF-8":
            header = {
                "X-Zn-Open-App-Id":application_id,
                "X-Zn-Open-App-Key":application_key,
                "X-Zn-Content-MD5":self.contentMD5(),
                "Content-Type":content_type,
                "X-Zn-Open-Request-Id":request_id,
                "X-Zn-Open-Timestamp":self.timeStamp(),
                "X-Zn-Open-Signature": h.creatSigna()
            }

        else:
            header = {
                "X-Zn-Open-App-Id": application_id,
                "X-Zn-Open-App-Key": application_key,
                "X-Zn-Content-MD5": "",
                "Content-Type": content_type,
                "X-Zn-Open-Request-Id": request_id,
                "X-Zn-Open-Timestamp": self.timeStamp(),
                "X-Zn-Open-Signature": h.creatSigna()
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
        print('X-Zn-Open-Signature:', header['X-Zn-Open-Signature'])

    # def witerHeaderToExcel():
    #     pass

h = Header(method, content_type, request_path, body)

h.creatHeader()


