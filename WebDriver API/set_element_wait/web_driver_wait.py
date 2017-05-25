# 显示等待，在等待某个条件成立时继续执行，否则在达到最大时长时抛出异常（TimeoutException）

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # 通过as将expected_conditions重命名为EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

# driver为浏览器驱动，30为最长超时时间，0.5为检测的间隔时长
# 这里表示在30S内每个0.5S就去查下id = "KW"是否被加在DOM树里，找不到就报默认的NosuchElementException异常
element = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, "kw"))) # 大坑，记住这里元素定位要大写
element.send_keys("selenium")

driver.quit()