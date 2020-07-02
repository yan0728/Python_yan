#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = ''
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit5").click()

driver.find_element_by_id("com.android.calculator2:id/mul").click()

driver.find_element_by_id("com.android.calculator2:id/digit9").click()

driver.find_element_by_id("com.android.calculator2:id/minus").click()

driver.find_element_by_id("com.android.calculator2:id/digit9").click()
driver.find_element_by_id("com.android.calculator2:id/equal").click()
test = driver.find_element_by_class_name("android.widget.EditText").text
print("结果="+test)
if test == 36:
    print("正确")
else:
    print("结果错误")
driver.quit()