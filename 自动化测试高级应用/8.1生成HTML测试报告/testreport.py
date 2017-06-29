from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Baidutest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def test_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        for i in range(60):
            try:
                if driver.title == u"HTMLTestRunner_百度搜索":
                    break
            except:pass
            time.sleep(1)
        else:
            self.fail("time out")
        self.assertEqual(driver.title, u"HTMLTestRunner_百度搜索")
        try:
            self.assertEqual(driver.title, u"HTMLTestRunner_百度搜索")
        except BaseException as error:
            print(error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Baidutest("test_search"))

    # 定义测试报告存放路径
    fp = open(r'C:\Users\Administrator\Desktop\report.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u'百度搜索测试报告',
                            description=u'用例执行情况：')

    runner.run(suite)
    fp.close()