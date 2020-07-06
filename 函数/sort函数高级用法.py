#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: sort函数高级用法.py
@time:2020/7/6 0006
"""
# sort 函数回归,正序排练
a = [3,4,5,6,7,89,10]
a.sort()
# print(a)

# sort函数reverse参数（反转）
a.sort(reverse=True)
# print(a)

#sort 函数key参数
# 函数也可以当做参数传递到其他函数中
b = [{'id':'1','age':18,'name':'yan'},{'id':'1','age':17,'name':'yan'},{'id':'1','age':20,'name':'yan'}]

def sort_key(x): # x 等于每个字典
    return x['age']
b.sort(key=sort_key,reverse=True)

print(b)