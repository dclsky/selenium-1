from selenium import webdriver
import time, os # 导入os模块，os模块中的path.abspath可以获取当前路径下的文件

driver = webdriver.Chrome()
driver.implicitly_wait(10)
file_path = "file:///" + os.path.abspath("frame.html")
driver.get(file_path)

# 先定位到iframe(id = "f1")
driver.switch_to.frame("f1")

# 再定位到iframe(id = "f2")
driver.switch_to.frame("f2")

# 正常操作页面元素
driver.find_element_by_link_text("hao123").click()

# 后退到之前的页面
driver.back()

# 跳回iframe(id = "f1")
driver.switch_to.parent_frame()

# 利用xpath定位该层的标题并打印
text1 = driver.find_element_by_xpath('html/body/div[1]/div/h3').text
print(text1)

# 跳回最外层的页面
driver.switch_to.default_content()

# 利用xpath定位最外层的标题并打印
text2 = driver.find_element_by_xpath('html/body/div[1]/div/h3').text
print(text2)

driver.quit()