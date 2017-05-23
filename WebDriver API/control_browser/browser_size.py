from selenium import webdriver
import time # 导入时间模块

driver = webdriver.Chrome()
driver.get("https://m.baidu.com/")

# 设置浏览器为宽480，高800显示
print("设置浏览器为宽480，高800显示")
driver.set_window_size(480,800)
time.sleep(3) # 添加休眠时间3秒
driver.quit()