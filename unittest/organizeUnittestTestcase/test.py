from calculator import Calculator
import unittest

class Test_add(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_add(self):
        a = Calculator(1, 2)
        self.assertEqual(a.add(), 3)

    def tearDown(self):
        print("test end")

class Test_sub(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_sub(self):
        a = Calculator(1, 2)
        self.assertEqual(a.sub(), -1)

    def tearDown(self):
        print("test end")

class Test_mul(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_mul(self):
        a = Calculator(1, 2)
        self.assertEqual(a.mul(), 2)

    def tearDown(self):
        print("test end")

class Test_div(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_div(self):
        a = Calculator(1, 2)
        self.assertEqual(a.div(), 0.5)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    #
    suite = unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_sub("test_sub"))
    suite.addTest(Test_mul("test_mul"))
    suite.addTest(Test_div("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
