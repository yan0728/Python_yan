#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 继承.py
@time:2020/7/10 0010
"""

#  面向对象有三个特性：封装/继承/多态

# 继承
class Persion(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name,"吃饭")

    def run(self):
        print("一个",self.age,"岁的小孩在奔跑")

# Student 继承了
class Student(Persion):
    pass

s = Student('yanxuelei',18)
s.eat()
s.run()