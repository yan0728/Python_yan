#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 将多个测试分到一个类中.py
@time:2021/1/28 0028
"""
import pytest

class TestClass():
    def test_one(self):
        x = 'this'
        assert 'h' in x

    # hasattr() 函数用于判断对象是否包含对应的属性。如果对象有该属性返回 True，否则返回 False。

    def test_two(self):
        x = 'hello'
        assert hasattr(x,"check")


'''
 class Coordinate:
 x = 10
 y = -5
 z = 0

point1 = Coordinate() 
print(hasattr(point1, 'x')) True
print(hasattr(point1, 'y')) True
print(hasattr(point1, 'z')) True
print(hasattr(point1, 'no')) False # 没有该属性
 '''