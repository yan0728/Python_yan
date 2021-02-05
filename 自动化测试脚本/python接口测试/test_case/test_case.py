#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:3021/1/7 0007
"""

import requests
import json
from 自动化测试脚本.python接口测试.test_data import testdata
from 自动化测试脚本.python接口测试.config import ReadConfig
def test_1118():
    global consultId
    url = ReadConfig.base_url + testdata.api1118
    data = testdata.data1118
    header = ReadConfig.header
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("请求数据:", data)
    print("-" * 30,"美丽的分界线","-" * 30)
    print("返回数据", r.text)
    assert r.status_code == 200
    consultId =  (r.json()["responseBody"]["consultId"]) #r.json后变成字典
    return consultId

def test_1037():
    url = ReadConfig.base_url + testdata.api1037
    data = testdata.data1037
    header = ReadConfig.header
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("请求数据:",data)
    print("-" * 30, "美丽的分界线", "-" * 30)
    print("返回数据", r.text)
    assert r.status_code == 201

def test_1084():
    url = ReadConfig.base_url + testdata.api1084
    data = testdata.data1084
    header = ReadConfig.header
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("请求数据:",data)
    print("-" * 30, "美丽的分界线", "-" * 30)
    print("返回数据", r.text)
    assert r.status_code == 201


def test_1038():
    url = ReadConfig.base_url + testdata.api1038
    data = testdata.data1038
    header = ReadConfig.header
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("请求数据:",data)
    print("-" * 30, "美丽的分界线", "-" * 30)
    print("返回数据",r.text)
    assert r.status_code == 201


def test_1049():
    url = ReadConfig.base_url + testdata.api1049
    data = testdata.data1049
    header = ReadConfig.header
    r = requests.post(url=url,data=json.dumps(data) ,headers=header)
    print("请求数据:",data)
    print("-" * 30, "美丽的分界线", "-" * 30)
    print ("返回数据",r.text)
    assert r.status_code == 201



