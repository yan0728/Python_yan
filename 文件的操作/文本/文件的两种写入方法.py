#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 文件的两种写入方法.py
@time:2020/7/9 0009
"""

# write函数：

# writelines函数：
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。换行需要制定换行符 \n。

fp = open('test.txt','w')
str = ['a\n','b\n','c']
fp.writelines(str)
fp.close()