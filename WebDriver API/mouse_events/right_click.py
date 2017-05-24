# context_click()方法可以模拟鼠标右击操作
from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com/")

# 定位到要右击的元素
right_click = driver.find_element_by_id("XXX")
# 对定位到的元素执行鼠标右击操作
ActionChains(driver).context_click(right_click).perform()