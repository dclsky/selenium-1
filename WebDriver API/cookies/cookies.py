from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10) # 设置全局隐式等待10S
driver.get('http://192.168.200.128/phpwind/')

# 获取当前cookies并打印
cookies = driver.get_cookies()
print('登陆前的cooikes：%s ' % cookies)

# 登录phpwind
driver.find_element_by_link_text('登录').click()
driver.find_element_by_name('pwuser').send_keys('github')
driver.find_element_by_name('pwpwd').send_keys('123456')
driver.find_element_by_name('submit').click()

# 获取登陆后cookies并打印
cookies = driver.get_cookies()
print('登陆后的cooikes：%s ' % cookies)

# 向cookie的name和value中添加会话信息
driver.add_cookie({'name':'key-name','value':'key-value'})

# 遍历cookies中的name和value信息并打印，包括上面添加的信息
for cookie in cookies:
    print('%s -> %s' % (cookie['name'],cookie['value']))

driver.quit()