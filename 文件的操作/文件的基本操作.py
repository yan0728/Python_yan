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

#写入文件 使用w  python3编码不是utf-8 因此需要使用encoding,如图文件存在将会覆盖掉
# file = open('test.txt','w',encoding='utf-8')
# file.write('闫学雷zs')
# file.close()

# a追加方式打开文件，不能用于读
# a:append
# file = open('test.txt','a',encoding='utf-8')
# file.write('yangxuelei')
# file.close()

# r+ 读写方式打开文件


# w+读写方式打开文件


# a+追加和读的方式打开文件