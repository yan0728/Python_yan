#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: testCase.py
@time:2021/1/5 0005
"""
import unittest
import requests
import json
from 自动化测试脚本.python接口测试.config import ReadConfig
from 自动化测试脚本.python接口测试.test_data import testdata
url = ReadConfig.base_url + testdata.api1118
data = testdata.data1118
header = testdata.header



class Test3(unittest.TestCase):
    def test_one(self):
        print('execute test_one')

    def test_two(self):
        print('execute test_two')

    def test_1118(self):
        r = requests.post(url=url,data=json.dumps(data) ,headers=header)
        try:
            assert r.status_code == 2001
            print ("1118接口正确")
        except :
            print("1118接口错误", r.text )