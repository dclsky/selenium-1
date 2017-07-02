# -*- coding: utf-8 -*-
'''
@author : Ben
对phpwind论坛的注册进行简单的测试
'''
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Registertest(unittest.TestCase):
    '''注册测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://192.168.134.129/phpwind/register.php"

    def test_register(self):
        '''验证正常输入各项数据注册成功'''
        driver = self.driver
        driver.get(self.url)
        user =  time.strftime("%H%M%S")
        driver.find_element_by_name("regname").send_keys(user)
        driver.find_element_by_name("regpwd").send_keys("123456")
        driver.find_element_by_name("regpwdrepeat").send_keys("123456")
        driver.find_element_by_name("regemail").send_keys(user+"@qq.com")
        driver.find_element_by_name("rgpermit").click()
        driver.find_element_by_class_name("btn").click()
        # 添加显示等待
        username = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, "td_userinfo_more")))
        # 对测试结果进行断言
        self.assertEqual(username.text, user)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()