#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 列表生成式.py
@time:2020/7/22 0022
"""
# 列表生成器
# values = [x for x in range(0,101)]
# print(values)

# 获取1-100之间所有的偶数
valus = [x for x in range(1,101) if x%2 ==0 ]
print(valus)