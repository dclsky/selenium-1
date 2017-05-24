# 模拟鼠标悬停操作
from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 定位到要悬停的元素
hover = driver.find_element_by_link_text("设置")
# 对定位到元素执行悬停操作
ActionChains(driver).move_to_element(hover).perform()

time.sleep(3)
driver.quit()

