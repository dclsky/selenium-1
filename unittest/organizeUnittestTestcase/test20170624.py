# 把setup和teardown封装起来
from calculator import Calculator
import unittest

class Mytest(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Test_add(Mytest):

    def test_add(self):
        a = Calculator(1, 2)
        self.assertEqual(a.add(), 3)

class Test_sub(Mytest):

    def test_sub(self):
        a = Calculator(1, 2)
        self.assertEqual(a.sub(), -1)

class Test_mul(Mytest):

    def test_mul(self):
        a = Calculator(1, 2)
        self.assertEqual(a.mul(), 2)

class Test_div(Mytest):

    def test_div(self):
        a = Calculator(1, 2)
        self.assertEqual(a.div(), 0.5)

if __name__ == '__main__':
    unittest.main()

