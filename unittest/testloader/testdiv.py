from calc import Calc
import unittest

class Test_div(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_div1(self):
        a = Calc(1,2)
        self.assertEqual(a.div(), 0.5)

    def test_div2(self):
        b = Calc(3,4)
        self.assertEqual(b.div(), 0.75)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()

