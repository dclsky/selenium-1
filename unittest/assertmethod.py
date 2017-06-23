import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_assert_equal(self): # a = b
        a = 1
        b = 1
        self.assertEqual(a, b, msg="a!=b")

    def test_assert_not_equal(self): # a != b
        c = 1
        d = 2
        self.assertNotEqual(c, d, msg="c = d")

    def test_assert_true(self): # bool(x） is True
        e = 1
        self.assertTrue(e > 0, msg="e <= 0")

    def test_assert_false(self): # bool(x) is False
        f = 1
        self.assertFalse(f > 2, msg="f <= 2")

    def test_assert_is(self): # a is b
        g = 1
        self.assertIs(g, 1, msg="g is not 1")

    def test_assert_is_not(self): # a is not b
        h = 1
        self.assertIsNot(h, 2, msg="g is 1")

    def test_assert_is_none(self): # x is None
        i = None
        self.assertIsNone(i, msg="i is not None")

    def test_assert_is_not_none(self): # x is not None
        j = 1
        self.assertIsNotNone(j, msg="j is None")

    def test_assert_in(self): # a in b
        k = 'hello'
        l = 'hello, world'
        self.assertIn(k, l, msg="a is not in b")

    def test_assert_not_in(self): # a not in b
        m = 'hello'
        n = 'hey'
        self.assertNotIn(m, n, msg="m is in n")

    def test_assert_isinstance(self): # isinstance(a, b)
        o = 1
        self.assertIsInstance(o, int, msg="o is not int")

    def test_assert_not_isinstance(self): # not isinstance(a, b)
        p = 'monday'
        self.assertNotIsInstance(p, int, msg="p is int")

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()