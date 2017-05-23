from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

# 刷新页面
print("刷新页面")
driver.refresh()
time.sleep(3)

driver.quit()
