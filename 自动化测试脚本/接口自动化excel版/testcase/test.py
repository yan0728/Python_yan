#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: Faker实战教程.py
@time:2021/2/5 0005
"""

import requests
from 自动化测试脚本.接口自动化excel版.uti import ReadExcel,WriteResult
from 自动化测试脚本.接口自动化excel版.setting import config
import json

exceldata = ReadExcel.ReadExcel.getExcelData1026()
for i in range(0, len(exceldata)):
    params = exceldata[i]
    if params['method'] == 'post':
        params = exceldata[i]
        if params['method'] == 'post':
            print("post")
    else:
        print("get")