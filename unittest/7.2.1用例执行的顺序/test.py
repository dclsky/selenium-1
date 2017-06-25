# unittes框架默认按0~9，A~Z，a~z的顺序执行测试用例，并不是按从上到下顺序执行
import unittest

class TestBbb(unittest.TestCase):

    def setUp(self):
        print("test TestBbb:")

    def test_ccc(self):
        print("test_ccc")

    def test_bbb(self):
        print("test_bbb")

    def tearDown(self):
        pass

class TestAaa(unittest.TestCase):

    def setUp(self):
        print("test TestAaa:")

    def test_fff(self):
        print("test_fff")

    def test_aaa(self):
        print("test_aaa")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
