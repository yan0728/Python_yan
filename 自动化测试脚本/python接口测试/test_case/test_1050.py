#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: test_1119.py
@time:2021/1/15 0015
"""
import requests
import json
import pytest
from 自动化测试脚本.python接口测试.test_data import testdata
from 自动化测试脚本.python接口测试.config import ReadConfig
url = ReadConfig.base_url + testdata.api1050
data = testdata.data1050
header = testdata.header

def test_1050():
    r = requests.post(url = url,data = json.dumps(data),headers = header)
    try:
        assert r.status_code == 200
        print("1050接口正确")
    except:
        print("1050接口错误:",r.text )

