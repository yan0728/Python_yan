#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: with语句优化文件操作.py
@time:2020/7/9 0009
"""

# with as 的方式写 会自动关闭文件
with open('test.txt','r',encoding='utf-8') as fp: # 等于 fp = open('test.txt','r',encoding='utf-8')
    #遍历指针
    for i in fp:
        print(i)