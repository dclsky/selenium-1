from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner # 导入HTMLTestRunner模块

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
        # 在60S内每隔1S检测当前页面标题是否等于预期标题
        for i in range(60):
            try:
                if driver.title == u"HTMLTestRunner_百度搜索":
                    break
            except:pass
            time.sleep(1)
        else:
            self.fail("time out")
        # 对标题进行断言
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
    # 通过open()方法打开C:\Users\Administrator\Desktop\report.html，没有则自动创建该文件
    fp = open(r'C:\Users\Administrator\Desktop\report.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, # stream制定测试报告文件
                            title=u'百度搜索测试报告',  # title定义测试报告标题
                            description=u'用例执行情况：') # description定义测试报告副标题

    runner.run(suite) # 通过HTMLTestRunner的run()方法来运行测试套件
    fp.close() # 关闭测试报告