# -*- coding:utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
import time
# import random
# import random as r
# # import cx_Oracle
# import os
from TestData import get_idcard,get_phone,get_name,get_number
name = ('时供应商客服二 ','时供应商客服一','时项目公司客服一','时项目公司客服二 ')
username = 'admin'
password = '123456'
# auto = webdriver.Chrome()
driverfile_path = r'D:\Program Files\Python38\msedgedriver.exe'
auto = webdriver.Edge()
auto.get("https://test-asos.lianjieabs.com/task/index")
time.sleep(3)
auto.maximize_window()
auto.find_element_by_id("username").send_keys(username)
auto.find_element_by_id("password").send_keys(password)
auto.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
for i in range(len(name)):
    auto.find_element_by_xpath('//div[2]/span').click()
    time.sleep(1)
    auto.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(name[i])
    auto.find_element_by_xpath("//button[contains(.,'查 询')]").click()
    time.sleep(1)
    auto.find_element_by_xpath('//div[contains(@class, "ant-tabs-content")]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/button').click()
    auto.find_element_by_id("coordinated_authorizer_idNumber").send_keys(get_idcard())
    auto.find_element_by_xpath("//div[6]/div/div/div/div").click()
    auto.find_element_by_xpath("//li[contains(.,'审核通过')]").click()
    auto.find_element_by_xpath("//div[@id='coordinated_gender']/div/div/div").click()
    auto.find_element_by_xpath("//li[contains(.,'否')]").click()
    auto.find_element_by_xpath("//div[4]/div[4]/div/div/div/div").click()
    auto.find_element_by_xpath("(//div[@id='test-uuid']/ul/li[2])[3]").click()
    time.sleep(1)
    auto.find_element_by_xpath("//button[contains(.,'审核完成')]").click()
    auto.find_element_by_xpath("//button[contains(.,'确 定')]").click()
    time.sleep(1)
auto.find_element_by_xpath("//span[2]/span[2]").click()
time.sleep(1)
auto.find_element_by_xpath("//a[contains(.,'退出登录')]").click()
auto.find_element_by_xpath("//button[contains(.,'确 定')]").click()
time.sleep(1)
auto.close()