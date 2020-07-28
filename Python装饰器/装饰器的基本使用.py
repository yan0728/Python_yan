#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 装饰器的基本使用.py
@time:2020/7/28 0028
"""
user = {
    'username':True,
    'age': 30
}
# case1
# if user['username'] == 'yan' and user['age'] == 30:
#     print('登录成功')
# else:
#     print('登录失败')

# case2
# def login_requert(func):
#     if user['username'] == True:
#         func()
#     else:
#         zhuce()
# def writ_word():
#     print("写文章")
#
# def add_word():
#     print("添加文章")
#
# def zhuce():
#     print('去注册')
# login_requert(writ_word)
# login_requert(add_word)

# case 3
def login_requese(func):
    def wapper():
        if user['username'] == True:
            func()
        else:
            print("跳转到登录页面")
    return wapper

@login_requese #装饰器装饰函数，调用edit_username的时候，会把edit_username传递给login_request里面，并先执行login_request方法
def edit_username():
    print("username修改成功")

@login_requese
def add_writer():
    print("文章添加成功")

add_writer()