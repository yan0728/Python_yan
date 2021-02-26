#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: test.py
@time:2021/2/25 0025
"""
import random
a = ['日升','分米鸡','戈拿旺','羊庄','海底捞','比格']
food = random.choice(a)
if food == '海底捞':
    print(food)
else:
    print(a[4])