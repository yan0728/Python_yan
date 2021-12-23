from selenium import webdriver
import time

#  学习地址https://www.jianshu.com/p/1531e12f8852
# https://www.bootwiki.com/selenium/index.html

# unitest -- 单元测试框架
# https://docs.python.org/zh-cn/3.7/library/unittest.html#

# 启动浏览器
driverfile_path = r"D:\pythonProject\Python_yan\chromedriver.exe"
driver = webdriver.Chrome(service=driverfile_path) # 声明浏览器

# driver = webdriver.Chrome()
base_url = 'https://test-bifang.lianjieabs.com/login'
driver.maximize_window() #最大化
driver.get(base_url) # 访问网页











# 元素定位
# def test_one():
#     browser.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[3]/div[2]/div[2]/div[3]/div[2]/div").click()
#
# def test_two():
#     browser.find_element_by_class_name("c-gap-bottom-small").click()
#
# if __name__ == '__main__':
#     time.sleep(10)
#     test_one()
#     # test_two()
#     browser.quit()