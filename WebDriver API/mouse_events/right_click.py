from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com/")

driver.find_element_by_link_text("帐号密码登录").click()

right_click = driver.find_element_by_id("s_lg_img")
ActionChains(driver).context_click(right_click).perform()