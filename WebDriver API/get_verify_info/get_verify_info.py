from selenium import webdriver
import time # 导入时间模块

# 打开phpwind论坛页面
driver = webdriver.Chrome()
driver.get("http://192.168.200.128/phpwind/")

# 执行登陆操作
driver.find_element_by_link_text("登录").click()
driver.find_element_by_name("pwuser").send_keys("github")
driver.find_element_by_name("pwpwd").send_keys("123456")
driver.find_element_by_name("submit").click()
time.sleep(3)

# 获取当前登陆用户名，并打印
print(driver.find_element_by_id("td_userinfo_more").text)
# 获取当前网页标题，并打印
print(driver.title)
# 获取当前网页链接，并打印
print(driver.current_url)
time.sleep(3)


# 退出登陆
driver.find_element_by_link_text("退出").click()