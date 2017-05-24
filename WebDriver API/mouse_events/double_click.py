# double_click()方法可以模拟鼠标双击操作
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("XXX")

# 定位到要双击的元素
double_click = driver.find_element_by_id("XXX")
# 对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()