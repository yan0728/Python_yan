import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random

# 驱动文件路径
# driverfile_path = r'D:\pythonProject\Python_yan\chromedriver.exe'

driverfile_path = r'D:\Program Files\Python38\msedgedriver.exe'
# browser = webdriver.Chrome()
browser = webdriver.Edge()
base_url = 'https://test-asos.lianjieabs.com/task/index'
browser.maximize_window()
browser.get(base_url) # 访问网页

name = ('时供应商客服二 ','时供应商客服一','时项目公司客服一','时项目公司客服二 ')
username = 'admin'
password = '123456'

