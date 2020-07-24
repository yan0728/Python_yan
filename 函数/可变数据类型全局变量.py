#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 可变数据类型全局变量.py
@time:2020/7/6 0006
"""

PER = []

def xiu_gai(per):
    PER.append(per)
    print(PER)

xiu_gai({'id:1,name:yanxuelei'})