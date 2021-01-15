#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:2021/1/7 0007
"""

import requests
import json
# import pytest
from 自动化测试脚本.python接口测试.test_data import testdata
from 自动化测试脚本.python接口测试.config import config

# Pytest+Request+Allure+Jenkins
url = config.base_url + testdata.api1118
data = testdata.data1118
header = config.header
def test_1118(url,data):

    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    # print(r.text)
    return r.status_code,r.text

def test_assert_1118():
    try:
        # 获取1118接口的返回值
        status_code , text = test_1118(url,data)
        assert status_code == 200
        print ("1118接口正确")
    except :
        print("1118接口错误", text )
if __name__ == '__main__':
    test_1118(url, data)
    test_assert_1118()