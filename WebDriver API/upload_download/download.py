from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://pypi.python.org/pypi/selenium#downloads")

# 定位到下载按钮，并点击
driver.find_element_by_link_text("selenium-3.4.3-py2.py3-none-any.whl").click()