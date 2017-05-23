from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

# 获得输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

# 获得百度页面底部备案信息
text = driver.find_element_by_id("cp").text
print(text)


# 获取当前网页标题
title = driver.title
print(title)

# 获取当前网页链接
url = driver.current_url
print(url)

# 返回元素“kw”的属性值
attribute = driver.find_element_by_id("kw").get_attribute("type")
print(attribute)

# 返回元素的结果是否可见
result = driver.find_element_by_id("kw").is_displayed()
print(result)

time.sleep(3)
driver.quit()