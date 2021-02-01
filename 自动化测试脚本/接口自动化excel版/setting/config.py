#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: config.py
@time:2021/2/1 0001
"""

import os
import time

BAST_PATH = os.path.dirname(os.path.dirname(__file__))
print(BAST_PATH)

# 根目录地址

TEST_CASE_PATH = os.path.join(BAST_PATH,'data','测试数据.xlsx')


report_time = time.strftime("%Y-%m-%d %H-%M-%S")
print(report_time)