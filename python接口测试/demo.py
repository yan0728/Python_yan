#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:2021/1/7 0007
"""

import requests
import json
import urllib.request
import urllib.parse

# base_url = 'http://loan-api-link.asset.jc4.jieyue.com'
# api = '/loan-api-link/api/appbiz/LoanEasyRest/1118/v1'
# url = base_url + api

r = requests.get('http://www.baidu.com')
# 查看响应内容，response.text 返回的是Unicode格式的数据
# print(json.dumps(r.text))

# 查看响应码
print(r.status_code)