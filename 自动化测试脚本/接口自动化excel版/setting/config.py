#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: config.py
@time:2021/1/22 0022
"""

import os
import time

# 集成路径
BASE_PATH = os.path.dirname((os.path.dirname(__file__)))
# print(BASE_PATH)

# 测试案例储存路径
file_path = '测试数据.xlsx'
TEST_CASE_PATH = os.path.join(BASE_PATH,'data',file_path)

# 测试报告储存路径
report_time = time.strftime('%Y-%m-%d %H:%M:%S')
TEST_REPORT = os.path.join(BASE_PATH,'report',report_time+'report.html')

