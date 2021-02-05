#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: config.py
@time:2021/1/15 0015
"""

import configparser
import os


'''
注：
__file__是当前执行的文件
os.path.dirname() 是 获取路径中的目录名
这样可以使用 BASE_DIR 进行相关操作，而不用担心路径问题
'''
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()  #创建一个实例

# 读取config.ini
config.read(BASE_DIR+"\\config\\config.ini")

# 读取 [TESTBASE] 分组下的 base_url 的值
base_url = config.get("TESTBASE","base_url4")
header = eval(config.get("TESTBASE","header"))