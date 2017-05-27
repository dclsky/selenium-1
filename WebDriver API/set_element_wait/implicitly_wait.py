# 隐性等待对整个driver的周期都起作用，所以只要设置一次即可
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()

#设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("https://translate.google.cn/")

try:
    print(ctime()) # 打印当前时间
    text = driver.find_element_by_id("gt-appname").text
    print(text)
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()