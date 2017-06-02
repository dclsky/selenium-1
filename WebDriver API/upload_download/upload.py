from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("upload_file.html")
driver.get(file_path)

# 定位到上传按钮，通过send_keys()方法添加本地文件
driver.find_element_by_xpath("html/body/div[1]/div/input").send_keys("E:\\README.md")

driver.quit()