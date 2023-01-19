# -*- coding: utf-8 -*-
"""
@time :    2023/1/19  11:44
@File:     config.py
@Software: PyCharm
@Author :  yanxuelei
@Version:  python3.8
"""

import os
import time

# 根目录地址
BAST_PATH = os.path.dirname(os.path.dirname(__file__))
# print(BAST_PATH)

BAST_URL = "http://123.57.27.89"

TEST_CASE_PATH = os.path.join(BAST_PATH, "data", "测试数据.xlsx")
# print(TEST_CASE_PATH)

TEST_LOG = os.path.join(BAST_PATH, "log", time.strftime("%Y-%m-%d") + ".log")
report_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(report_time)