#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 被装饰的函数需要带参数.py
@time:2020/7/28 0028
"""
user = {
    "login" : True
}

def login_request(func):
    # 使用位置参数和关键子参数代替参数
    def wapper(*args,**kwargs):
        if user["login"] == True:
            func(*args,**kwargs)
        else:
            print('请先登录')
    return wapper
@login_request
def edit_user(username):
    print('用户名修改为{}'.format(username))

@login_request
def add_wenzhang(title,content):
    print('文字的标题是{},文章的内容是{}'.format(title,content))

edit_user('yanxuelei')

add_wenzhang('this is title',' 这是内容 ')

