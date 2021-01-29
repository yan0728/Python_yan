#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: name变量的使用.py
@time:2020/7/22 0022
"""

def name():
    print('my is name')

#如果当前文件是主运行文件，将会执行name这个函数
if __name__ == '__main__':
    name()