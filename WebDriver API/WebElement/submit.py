# submit()方法用于提交表单，可以通过submit()方法模拟在搜索框输入关键字之后的“回车”操作
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

driver.find_element_by_id("lst-ib").send_keys("百度一下，你就知道")
driver.find_element_by_class_name("lsb").submit()

time.sleep(3)

driver.quit()