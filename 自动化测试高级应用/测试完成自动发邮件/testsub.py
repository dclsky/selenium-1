from calc import Clac # 从calc模块中导入Clac类
import unittest # 导入单元测试框架

# 定义减法测试类，并继承unittest的TestCase类
class Testsub(unittest.TestCase):
    '''减法测试'''

    # 定义具体的减法测试方法
    def test_sub1(self):
        s1 = Clac(6, 5)
        self.assertEqual(s1.sub(), 1, 'your calculate is wrong')

    def test_sub2(self):
        s2 = Clac(6, 1)
        self.assertEqual(s2.sub(), 5, 'your calculate is wrong')

if __name__ == '__name__':
    unittest.main()
