from calc import Calc
import unittest

class Test_sub(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_sub1(self):
        a = Calc(1,2)
        self.assertEqual(a.sub(), -1)

    def test_sub2(self):
        b = Calc(3,4)
        self.assertEqual(b.sub(), -1)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()

