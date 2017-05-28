# 定位一组元素
from selenium import webdriver
import os, time # 导入os模块，os模块中的path.abspath可以获取当前路径下的文件

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("checkbox.html")
driver.get(file_path)

# 定位所有标签名为input的元素
elements = driver.find_elements_by_tag_name("input")
print(len(elements))

# 从定位的一组元素中过滤出type为checkbox的元素，并勾选中
for i in elements:
   if i.get_attribute('type') == 'checkbox':
       i.click()
time.sleep(2)

# 获取元素中第一个并取消勾选
elements.pop(0).click()
print(len(elements))
time.sleep(2)

# 利用xpath定位来勾选
xpath = driver.find_element_by_xpath("//*[@id='r1']")
xpath.click()
time.sleep(2)

driver.quit()

