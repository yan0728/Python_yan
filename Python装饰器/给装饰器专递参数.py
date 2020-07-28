#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 给装饰器专递参数.py
@time:2020/7/28 0028
"""
user = {
    "username": False
}

def login_request(site = 'front'):
    def outter_wapper(func):
        def inner_wapper(*args,**kwargs):
            if user["username"] == True:
                func(*args,**kwargs)
            else:
                if site == 'front':
                    print("跳转到前台登录")
                else:
                    print("跳转到后台登录")
        return inner_wapper
    return outter_wapper

@login_request('black')
def edit_user(newusername):
    print("用户名修改成{}".format(newusername))

edit_user('yan')