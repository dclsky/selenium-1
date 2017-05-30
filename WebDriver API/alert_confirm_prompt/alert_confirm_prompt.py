from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("alert_confirm_prompt.html")
driver.get(file_path)

driver.find_element_by_xpath("//*[@id='btnAlert']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='btnConfirm']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
time.sleep(3)

