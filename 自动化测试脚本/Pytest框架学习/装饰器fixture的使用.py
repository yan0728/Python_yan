#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 111.py
@time:2021/1/19 0019
"""
'''
方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
常用参数:
scope：被标记方法的作用域  session>module>class>function
function" (default)：作用于每个测试方法，每个test都运行一次
"class"：作用于整个类，每个class的所有test只运行一次 一个类中可以有多个方法
"module"：作用于整个模块，每个module的所有test只运行一次；每一个.py文件调用一次，该文件内又有多个function和class
"session：作用于整个session(慎用)，每个session只运行一次；是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
params：(list类型)提供参数数据，供调用标记方法的函数使用；一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它。
autouse：是否自动运行,默认为False不运行，设置为True自动运行；如果True，则为所有测试激活fixture func可以看到它。如果为False则显示需要参考来激活fixture<br><br>ids：每个字符串id的列表，每个字符串对应于params这样他们就是测试ID的一部分。如果没有提供ID它们将从params自动生成;是给每一项params参数设置自定义名称用，意义不大
'''


# !encoding=utf-8
import pytest

# 不带参数时默认scope="function",也就是只在test开头函数前后执行
@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print('用例1:登录之后其他动作111')

def test_s2():  # 不传login
    print('用例2:不需要登录，操作222')

def test_s3(login):
    print('用例3:登录之后其他动作333')

if __name__ == "__main__":
    pytest.main('-s')