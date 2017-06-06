from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)

# 截图当前窗口，并保存到相应位置，注意需要指定文件名和文件格式
driver.get_screenshot_as_file('E:\\baidu.jpg')

driver.close()