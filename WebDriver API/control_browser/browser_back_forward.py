from selenium import webdriver

driver = webdriver.Chrome()

# 访问百度首页
first_url = "http://www.baidu.com/"
print("now access %s" % (first_url))
driver.get(first_url)

# 访问百度贴吧
second_url = "https://tieba.baidu.com/index.html"
print("now access %s" % second_url)
driver.get(second_url)

# 后退到百度首页
print("back to %s" % (first_url))
driver.back()

# 前进到百度贴吧
print("forward to %s" % (second_url))
driver.forward()

driver.quit()