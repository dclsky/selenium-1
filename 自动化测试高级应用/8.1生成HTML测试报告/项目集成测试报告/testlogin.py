# -*- coding: utf-8 -*-
'''
@author : Ben
对phpwind论坛的登录进行简单的测试
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class Logintest(unittest.TestCase):
    '''登录测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://192.168.134.129/phpwind/login.php"

    def test_login1(self):
        '''验证账号密码正确登录成功'''
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_name("pwuser").send_keys("caoxin")
        driver.find_element_by_name("pwpwd").send_keys("123456")
        driver.find_element_by_name("submit").click()
        # 添加显示等待
        username = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID,"td_userinfo_more")))
        # 对测试结果进行断言
        self.assertEqual(username.text, "caoxin")

    def test_login2(self):
        '''验证账号密码不正确登录失败'''
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_name("pwuser").send_keys("test")
        driver.find_element_by_name("pwpwd").send_keys("1234567")
        driver.find_element_by_name("submit").click()
        username = WebDriverWait(driver, 30, 0.5).until(
            EC.presence_of_element_located(
                (By.XPATH,"//*[@id='main']/div[2]/table/tbody/tr[2]/td/center")))
        self.assertEqual(username.text, "用户test 不存在")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()