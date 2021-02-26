#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 111.py
@time:2021/2/26 0026
"""


x = 0
y = 1

for i in range(0,300):
    x = x+1
    if x % 30 == 0:
        y = y + 1
        print("x:{},y:{}".format(x,y))