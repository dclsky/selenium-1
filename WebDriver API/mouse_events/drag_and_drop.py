# drag_and_drop(source, target)在源元素上按住鼠标左键，然后移动到目标元素上释放
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("XXX")

# 定位到元素的原位置
source = driver.find_element_by_id("XXX")
# 定位到元素要移动到的目标位置
target = driver.find_element_by_id("XXX")
# 执行元素的拖放操作
ActionChains(driver).drag_and_drop(source, target).perform()