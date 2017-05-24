# 调用Keys()类的中方法模仿各种键盘操作
from selenium import webdriver
# 引入Keys模块
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# 输入框输入内容
driver.find_element_by_id("lst-ib").send_keys("githubb")
time.sleep(2)

# 删除多输入的的一个b
driver.find_element_by_id("lst-ib").send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 输入空格键 + “教程”
driver.find_element_by_id("lst-ib").send_keys(Keys.SPACE)
driver.find_element_by_id("lst-ib").send_keys("教程")
time.sleep(2)

# ctrl + a 全选输入框内容
driver.find_element_by_id("lst-ib").send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# ctrl + x 剪切输入框内容
driver.find_element_by_id("lst-ib").send_keys(Keys.CONTROL, 'x')
time.sleep(2)

# ctrl + v 粘贴内容到输入框
driver.find_element_by_id("lst-ib").send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 通过回车键来代替单击操作
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()