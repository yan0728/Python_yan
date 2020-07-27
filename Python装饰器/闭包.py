#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 闭包.py
@time:2020/7/27 0027
"""
# 如果在一个函数中，定义了另外一个函数，并且那个函数使用了外面函数的变量，并且外面那个函数返回了里面函数的引用
# 那么称为里面的这个函数为闭包,例如
# def greet(name):
#     def say_hello():
#         print('my name is {}'.format(name))
#     return say_hello #say_hello后面没有加（）代表，返回这函数的引用（并没有执行这个函数）
# ret = greet('yan') #ret 是say_hello函数的引用
# ret()  #调用ret函数

# 闭包下案例，计算器
# def calculator(option):
#     if option == 1:
#         def add(x,y):
#             return x + y
#         return add #返回的是add方法的引用
#     elif option == 2:
#         def subtraction(x,y):
#             return x - y
#         return subtraction
#     elif option == 3:
#         def multiplication(x,y):
#             return x * y
#         return multiplication
#     elif option == 4:
#         def division(x,y):
#             return x / y
#         return division
#     else:
#         print("输入错误")
#         return None
# add = calculator(1)
# ret = add(1,2) #调用add方法并赋值给ret
# print(ret)

# 函数内修改全局变量
# NUM = 10
# def add():
#     global NUM
#     NUM = NUM + 1
#     print(NUM)
# add()

# nonlocal 关键字与global 关键字相同，只是nonlocal在闭包的时候使用
# def greet(name):
#     def say_hello():
#         nonlocal name
#         name += ' hello'
#         print(name)
#     return say_hello
# ret = greet('yan')
# ret()

# 作业 y = x + 1 和 y = 2x + 1 使用闭包的方式
def opt(x):
    def add():
        return x + 1
    return add
ret = opt(1)
print(ret())
