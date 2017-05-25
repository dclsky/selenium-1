from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

print(ctime()) # 打印当前时间
# 通过for循环循环10次，每次判断id = "kw"的元素的is_displayed()是否为True，若为True则break跳出循环
# 否则sleep(1)后继续循环判断，知道10次循环结束，打印“time out”信息
for i in range(10):
    try:
        el = driver.find_element_by_id("kw")
        if el.is_displayed():
            break
    except:pass
    sleep(1)
else:
    print("time out")

driver.close()
print(ctime()) # 打印当前时间