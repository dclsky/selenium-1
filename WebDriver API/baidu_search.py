from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("python+selenium")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
