# 学习模块和类的fixtures
import unittest

def setUpModule(): # 测试模块执行前的初始化工作
    print("test module start >>>>>")

def tearDownModule(): # 测试模块执行后的善后工作
    print("test module end >>>>>")

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # 测试类执行前的初始化工作，需要用到装饰器@classmethod，且约定俗成的参数为cls
        print("test class start ......")

    @classmethod
    def tearDownClass(cls): # 测试类执行后的善后工作，需要用到装饰器@classmethod，且约定俗成的参数为cls
        print("test class end ......")

    def setUp(self):
        print("test start:")

    def tearDown(self):
        print("test end:")

    def test_case1(self):
        print("test case1")

    def test_case2(self):
        print("test case2")

if __name__ == '__main__':
    unittest.main()