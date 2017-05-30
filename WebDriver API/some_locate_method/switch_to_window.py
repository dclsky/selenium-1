from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com/")

# 获取当前百度首页窗口句柄
homepage_baidu = driver.current_window_handle

# 打开百度注册页面
driver.find_element_by_link_text("登录").click()
time.sleep(3)
driver.find_element_by_link_text("立即注册").click()

# 获取当前浏览器所有打开的窗口句柄
handles = driver.window_handles

# 进入注册窗口
for handle in handles:
    if handle != homepage_baidu:
        driver.switch_to.window(handle)
print(driver.title)

# 进入到百度首页窗口
for handle in handles:
    if handle == homepage_baidu:
        driver.switch_to.window(handle)
print(driver.title)




