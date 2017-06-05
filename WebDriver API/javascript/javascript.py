from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.cnblogs.com/yoyoketang/p/6128655.html')
driver.set_window_size(800,800) # 设置浏览器大小

# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(200,500);"
driver.execute_script(js)

# 滚动条到页面底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

# 滚动条到页面顶部
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

driver.quit()


