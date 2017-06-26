import unittest
from selenium import webdriver
import time

class Baidutest(unittest.TestCase):

    def setUp(self): # 测试前的准备工作，驱动初始化，设置隐形等待30S，设置基础URL地址
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(10)

    def test_search(self): # 谷歌搜索selenium
        driver = self.driver
        driver.find_element_by_id("lst-ib").send_keys("selenium")
        driver.find_element_by_class_name("lsb").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title,"selenium - Google 搜索",msg="搜索失败") # 对搜索后的标题进行断言

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()