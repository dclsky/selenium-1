# 练习使用unittest框架自带的装饰器
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    @unittest.skip("skip this testcase") # 无条件直接跳过测试
    def test_skip(self):
        print("test_skip:")

    @unittest.skipIf(3 > 2, "if true,skip this testcase") # 当条件为true时跳过测试
    def test_skipif(self):
        print("test_skipif:")

    @unittest.skipUnless(3 > 2, "only true will run this testcase") # 当条件为true时才执行测试
    def test_skipunless(self):
        print("test_skipunless:")

    @unittest.expectedFailure #将测试标记为失败
    def test_expectedfailure(self):
        print("test_expectedfailure:")

if __name__ == "__main__":
    unittest.main()