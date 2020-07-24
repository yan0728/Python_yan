#!/usr/bin/env python 
# try:
#     a = 1
#     b = 0
#     c = a/b
#     print(c)
#     print(d)
# except ZeroDivisionError: #除数是0的异常
#     print("发生异常执行")
# except NameError: #name异常
#     print("名字未定义")
# else:
#     print("没有发生异常执行")
# finally:
#     print("不管是否发生都执行")

# 自定义异常
# 抛出异常
def greet(name,age):
    if not isinstance(name,str):
        raise TypeError("姓名必须是字符类型")
    if not isinstance(age,int):
        raise TypeError("年龄必须是整形")
    print("姓名是{},年龄是{}".format(name,age))

try:
    greet(1,18)
except Exception as err: #Exception是所有异常都报
    print(err.args)


