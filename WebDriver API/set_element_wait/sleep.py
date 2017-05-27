from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://github.com/wycaoxin")

time.sleep(2) #sleep()方法表示代码运行到此处会等待一定的时长再继续运行
text = driver.find_element_by_class_name("js-repo").text
print(text)

time.sleep(2)
driver.quit()