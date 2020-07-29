#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 动态添加属性和方法.py
@time:2020/7/29 0029
"""
# 动态添加属性
# 1，通过 对象.属性的方法添加
class Persion(object):
    def __init__(self,name):
        self.name = name

p = Persion('yanxuelei')
# p.age = 18
# print(p.age)

# 通过setattr 函数添加
if not hasattr(p,'age'): #p对象是否有age属性
    setattr(p,'age',20) #添加属性方法 setattr(对象，属性，属性值)
print(p.age)


# 动态添加方法
