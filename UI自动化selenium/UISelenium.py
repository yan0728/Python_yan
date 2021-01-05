from selenium import webdriver
import time

#  学习地址https://www.jianshu.com/p/1531e12f8852
# https://www.bootwiki.com/selenium/index.html


# 启动浏览器
driverfile_path = r'D:\python37\PythonYan\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverfile_path) # 声明浏览器
base_url = 'http://www.baidu.com'
browser.maximize_window() #最大化
browser.get(base_url) # 访问网页

# 元素定位
def test_one():
    browser.find_element_by_id("kw").send_keys("selenium")
    browser.find_element_by_id("su").click()

def test_two():
    browser.find_element_by_class_name("c-gap-bottom-small").click()

# if __name__ == '__main__':
#     test_one()
#     test_two()
#     browser.quit()