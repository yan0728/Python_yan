#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:2020/8/27 0027
"""

from appium import webdriver
import time

calculator = {
    'platformName':'Android', # android的apk
    'deviceName':'QKKVFQNFEMV4QSGI', # 手机设备名称，通过adb devices查看
    'platformVersion':'9', # android系统的版本号
    'appPackage':'=com.tencent.mobileqq', # apk包名
    'appActivity':'com.tencent.mobileqq.activity.LoginActivity' # apk的launcherActivity
}
# 默认开启4723端口用于和android通讯
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',calculator)
time.sleep(2)


def cal():
    driver.find_element_by_id("com.android.calculator2:id/digit_7").click() # 用id元素定位到7
    driver.find_element_by_id("com.android.calculator2:id/op_add").click() # 用id元素定位到+
    driver.find_element_by_id("com.android.calculator2:id/digit_9").click() # 用id元素定位到9
    driver.find_element_by_id("com.android.calculator2:id/eq").click() # 用id元素定位到=
    driver.quit() # 运行完成后退出
# cal() #调用cal