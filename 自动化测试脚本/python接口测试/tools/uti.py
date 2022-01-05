#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: uti.py
@time:2021/2/5 0005
"""

import random
import time
from Faker实战教程 import Faker
f=Faker(locale='zh-CN')

frontTransNo = "2021"+str(random.randint(1000000,9999999))
ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
phone = "138"+ str(random.randint(10000000,99999999))
idCare = f.ssn() #身份证号
name = f.name()
email = f.email()
address = f.address()
