# 通过Testsuite类的addTest()方法使用例按照特定的顺序执行
import unittest
import test

# 构建测试套件
suite = unittest.TestSuite()
suite.addTest(test.TestBbb("test_ccc"))
suite.addTest(test.TestBbb("test_bbb"))
suite.addTest(test.TestAaa("test_fff"))
suite.addTest(test.TestAaa("test_aaa"))

# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)

