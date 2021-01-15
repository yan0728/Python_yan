#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:2021/1/7 0007
"""

import requests
import json
# get请求

# url = 'http://www.baidu.com'
# r = requests.get(url=url)
# print(r.status_code)

# post 请求
base_url = ' http://loan-api-link.asset.jc4.jieyue.com'
api = '/loan-api-link/api/appbiz/LoanEasyRest/1118/v1'
url = base_url + api
header = {'Content-Type': 'application/json;charset=UTF-8',
          'User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)',
          }
data = {
    "sysSource": "4",
    "frontTransNo": "20210107221401599",
    "frontTransTime": "2019-07-18 15:15:20",
    "interfaceNo": "1118",
    "busiCode": "CSB18",
    "telephone": "13916263326",
    "appAmount": "30000",
    "appPeriod": "24",
    "custmerManger": "11037385",
    "position": "301000817",
    "telemarketing": "0"
}
def test_1118(url,data):
    r= requests.post(url=url,data=json.dumps(data),headers=header)
    print(r.json())

test_1118(url,data)