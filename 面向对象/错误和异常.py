#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 错误和异常.py
@time:2021/1/28 0028
"""

'''
try 
    执行代码

except
    发生异常时执行的代码
    
else 
    没有异常是执行的代码
    
finally
    不管有没有异常都会执行的代码

'''

# while True:
#     num = input("请输入一个数字")
#     if int(num) != 111:
#         try:
#             print("try:执行了代码")
#             assert int(num)<10
#         except:
#             print("except:发生异常执行了代码")
#         else:
#             print("else:没有异常执行的代码")
#
#         finally:
#             print("finally:不管有没有异常都会执行的代码")
#     else:
#         print("退出")
#         break


'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：

raise [Exception [, args [, traceback]]]
'''


# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))


# try:
#         raise NameError('HiThere')
# except NameError:
#         print('An exception flew by!')
#         raise
