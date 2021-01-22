#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: ReqApi.py
@time:2021/1/22 0022
"""

import requests
from 自动化测试脚本.接口自动化excel版.uti import ReadExcel
import json

class SentRequest():

    def __init__(self):
        pass


    def sentRequest(self):
        exceldata = ReadExcel.ReadExcel.getExcelData(1)
        for i in range(0, len(exceldata)):
            params = exceldata[i]
            if params['method'] == 'post':
                r = requests.post(url=params['base_url']+params['api'],data=json.dumps(params['requestBody']),headers = eval(params['header']))
                print('接口:',params['base_url']+params['api'])
                try:
                    assert r.status_code == '200'
                    # return r.status_code
                    print(r.status_code)
                except:
                    # return r.text
                    print(params['api_name'],':',json.dumps(params['requestBody']),r.text)
            else:

                r = requests.get(url=params['base_url']+params['api'],data=params['requestBody'],headers = params['header'])
                try:
                    assert r.status_code == '200'
                    # return r.status_code
                    print( r.status_code)
                except:
                    print(r.text)
SentRequest.sentRequest(1)