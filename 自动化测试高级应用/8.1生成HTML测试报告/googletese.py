# -*- coding: utf-8 -*-
'''
@author : Ben
使用WebDriverWait和expected_conditions实现显示等待
'''
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait # 导入WebDriverWait模块
from selenium.webdriver.support import expected_conditions as EC # 导入expected_conditions模块，通过as关键字重命名为EC

class Googletest(unittest.TestCase):
    '''谷歌搜索测试'''

    def setUp(self):
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "https://www.google.com/"

    def test_google(self):
        '''搜索关键字：google'''
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("lst-ib").send_keys("google")
        driver.find_element_by_class_name("lsb").click()
        # 在30S内每隔0.5S检测当前页面标题是否等于“google - Google 搜索”
        WebDriverWait(driver, 30, 0.5).until(EC.title_is(u"google - Google 搜索"))
        # 对当前页面标题进行断言
        self.assertEqual(driver.title, u'google - Google 搜索')
        try:
            self.assertEqual(driver.title, u'google - Google 搜索')
        except BaseException as error:
            print(error)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    # 定义测试套件，并为测试套件添加测试用例
    suite = unittest.TestSuite()
    suite.addTest(Googletest('test_google'))
    # 定义测试报告存放路径
    fp = open(r'C:\Users\Administrator\Desktop\report.html','wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"google搜索",
                            description=u'google搜索测试用例')
    #执行测试，记得测试执行完要关闭测试报告
    runner.run(suite)
    fp.close()
