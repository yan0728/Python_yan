#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 类方法和静态方法.py
@time:2020/7/13 0013
"""

class Persion(object):

    guojia = 'china'

    def eat(self): #参数里面是self的代表是实例方法，需要对象调用
        print("人类在吃饭")

    @classmethod  #类方法需要使用装饰器
    def greet(cls): #第一个参数必须是cls，cls此时代表是Persion这个类，可以通过cls.guojia修改类方法
        print("我是类方法")
        cls.guojia = 'usa'

    # 静态方法不需要传递对象(self)或者类(cls)
    # 静态方法使用场景:不需要修改类或者对象的属性的时候，并且这个方法放到这个累中可以让让代码更有管理性
    @staticmethod
    def static_method():
        print("我是静态方法")

# 实例方法
p = Persion()
# p.eat()

# 类方法
# 1.调用类方法,使用类调用
# Persion.greet()
#  2.调用类方法，使用对象调用
p.greet()
# 3.通过类方法 修改类参数
print(Persion.guojia)

# 静态方法
# 1.类的方法调用
# Persion.static_method()
# 2.对象的方法调用
p.static_method()