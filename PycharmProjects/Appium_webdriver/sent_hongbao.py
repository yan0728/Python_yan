from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'huawei_mt7_tl00-P4M7N15204031162'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

driver.find_element_by_id("com.tencent.mm:id/n1").click()
# driver.find_element_by_id("com.tencent.mm:id/a2a").click()
# driver.find_element_by_id("com.tencent.mm:id/cau").click()
# driver.find_element_by_id("com.tencent.mm:id/a2f").click()
time.sleep(1)
driver.find_element_by_id("com.tencent.mm:id/a2e").click()
time.sleep(1)
driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[contains(@index,0)]").click()
time.sleep(5)
driver.find_element_by_id("com.tencent.mm:id/bbf").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_x").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_1").click()
driver.find_element_by_id("com.tencent.mm:id/b9v").click()
time.sleep(2)
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_1").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_1").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_5").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()


# i=0
# while i<5:
    # driver.find_element_by_id("com.tencent.mm:id/cau").click()
    # driver.find_element_by_id("com.tencent.mm:id/a2f").click()
    # i=i+1
print("send成功")
# driver.quit()