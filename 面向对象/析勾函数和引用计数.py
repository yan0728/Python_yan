#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 析勾函数和引用计数.py
@time:2020/7/7 0007
"""

# 析构函数 __del__方法 ，只要这个内存被是释放的时候就会调用这个函数
class Person(object):
    def __init__(self):
        self.name = 'yanxuelei'
        print("这是构造函数")
        self.file = open('xxx.txt','a', encoding='utf-8')

    def greet(self):
        print("我的名字是{}".format(self.name))

    def write(self):
        self.file.write('message')

    def __del__(self):
        print("我是析构函数")
        self.file.close() #析构函数一般用在文件操作完毕后关闭文件的时候调用
p = Person()
p.greet()
p.write()