from calc import Calc
import unittest

class Test_mul(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_mul1(self):
        a = Calc(1,2)
        self.assertEqual(a.mul(), 2)

    def test_mul2(self):
        b = Calc(3,4)
        self.assertEqual(b.mul(), 12)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()

