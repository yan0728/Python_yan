#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 装饰器pytest.mark.parametrize.py
@time:2021/1/21 0021
"""
import pytest
'''
在测试用例的前面加上：
@pytest.mark.parametrize("参数名",列表数据)
参数名：用来接收每一项数据，并作为测试用例的参数。
列表数据：一组测试数据。
'''

#====参数为列表嵌套字典====
def secend(c,b):
    add= int(b)+int(c)
    return add

@pytest.mark.parametrize('case',[{'b':'34','c':'56'},{'b':'39','c':'56'}])
def test_add01(case):
    tt=secend(**case)
    # print("测试账号：{}" .format(tt))
    print(1)

#====参数为列表嵌套元组====
test02_datas = [
    (11, 22, 33),
    (22, 33, 55)
]

@pytest.mark.parametrize("data", test02_datas)
def test_add02(data):
    res = data[0] + data[1]
    try:
     assert res == data[2]
     print(2)
    except :
        print("错误")

#====参数为列表嵌套列表====
test_datas = [
    [22, 33,55],
    [1, 2, 3]
]

@pytest.mark.parametrize("datalist", test_datas)
def test_add03(datalist):

    res = datalist[0] + datalist[1]
    assert res == datalist[2]
    print(3)

if __name__ == "__main__":

    pytest.main(["-s", "装饰器parametrize.py::::test_add03"])