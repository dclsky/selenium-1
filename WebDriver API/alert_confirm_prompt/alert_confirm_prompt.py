from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("alert_confirm_prompt.html")
driver.get(file_path)

# 点击alert弹窗并确定
driver.find_element_by_xpath("//*[@id='btnAlert']").click()
time.sleep(3)
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()
time.sleep(3)

# 点击confirm弹窗并确定
driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
time.sleep(3)
confirm1 = driver.switch_to.alert
print(confirm1.text)
confirm1.accept()
time.sleep(3)

# 点击confirm弹窗并取消
driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
time.sleep(3)
confirm2 = driver.switch_to.alert
print(confirm2.text)
confirm2.dismiss()
time.sleep(3)

# 点击prompt弹窗并输入"abc",然后点击确定
driver.find_element_by_xpath("//*[@id='btnPrompt']").click()
time.sleep(3)
prompt1 = driver.switch_to.alert
print(prompt1.text)
prompt1.send_keys('abc')
time.sleep(3)
prompt1.accept()
time.sleep(3)

# 点击prompt弹窗并输入"cba",然后点击取消
driver.find_element_by_xpath("//*[@id='btnPrompt']").click()
time.sleep(3)
prompt2 = driver.switch_to.alert
print(prompt2.text)
prompt2.send_keys('cba')
time.sleep(3)
prompt2.dismiss()
time.sleep(3)

driver.quit()