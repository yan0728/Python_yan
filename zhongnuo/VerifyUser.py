# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import random as r
import cx_Oracle
import os
from com.TestData import get_idcard,get_phone,get_name,get_number
username = ('18500000004','18500000004')
password = '123456'
auto = webdriver.Chrome()
auto.get("http://test-asms.lianjieabs.com/")
time.sleep(3)
auto.maximize_window()
for i in range(len(username)):
    auto.find_element_by_id("username").send_keys(username[i])
    auto.find_element_by_id("password").send_keys(password)
    auto.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    auto.execute_script('window.scrollTo(997472, document.body.scrollHeight)')
    time.sleep(2)
    auto.find_element_by_xpath("//button[contains(.,'同意并继续')]").click()
    time.sleep(1)
    auto.find_element_by_css_selector(".upload-content2 svg").click()
    time.sleep(1)
    os.system("D:\\VerifyUserUpload.exe")
    time.sleep(1)
    auto.find_element_by_css_selector(".upload-content3 svg").click()
    time.sleep(1)
    os.system("D:\\VerifyUserUpload.exe")
    time.sleep(2)
    auto.execute_script('window.scrollTo(2000, document.body.scrollHeight)')
    time.sleep(1)
    auto.find_element_by_css_selector('.avatar-uploader:nth-child(2) .cursor-pointer > .anticon use').click()
    time.sleep(1)
    os.system("D:\\VerifyUserUpload.exe")
    time.sleep(1)
    auto.find_element_by_xpath("//button[contains(.,'提交申请')]").click()
    time.sleep(1)
    auto.find_element_by_xpath("//button[contains(.,'确 定')]").click()
    time.sleep(1)
    auto.find_element_by_xpath("//div[@id='app']/section/section/div/header/div/div/div[2]/div/span/span[2]").click()
    time.sleep(1)
    auto.find_element_by_xpath("//span[contains(.,'退出登录')]").click()
    time.sleep(1)
    auto.find_element_by_xpath("//button[contains(.,'确 定')]").click()
time.sleep(2)
auto.close()