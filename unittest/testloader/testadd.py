from calc import Calc
import unittest

class Test_add(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add1(self):
        a = Calc(1,2)
        self.assertEqual(a.add(), 3)

    def test_add2(self):
        b = Calc(3,4)
        self.assertEqual(b.add(), 7)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()

