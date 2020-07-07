#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 文件的基本操作.py
@time:2020/7/7 0007
"""
# 1,打开文件 2,做相关操作 3.关闭文件
# 读取文件 使用r
# file = open('test.txt','r')
# str = file.read()
# print(str)
# file.close()

#写入文件 使用w  python3编码不是utf-8 因此需要使用encoding
file = open('test.txt','w',encoding='utf-8')
file.write('闫学雷')
file.close()