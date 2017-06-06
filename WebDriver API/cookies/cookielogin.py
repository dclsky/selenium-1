# 利用已经登录的cookie绕过登录验证
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://192.168.200.128/phpwind/')

# 将之前准备的cookie添加到cookies中
driver.add_cookie({'name':'25797_winduser','value':'AW1XVglZV1cODFEFBVIHDQRSVABVVF5UUwZYAAdSCwcBBjk%3D'})
print('cookies已添加，快见证这伟大的时刻吧')
driver.get('http://192.168.200.128/phpwind/')
time.sleep(3)

# 截图登录后的图片
driver.get_screenshot_as_file("E:\\phpwind.jpg")

# 获取登录后的用户名
username = driver.find_element_by_id('td_userinfo_more').text
if username == 'github':
    print('登录成功')

driver.quit()