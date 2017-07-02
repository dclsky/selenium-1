from calc import Clac # 从calc模块中导入Clac类
import unittest # 导入单元测试框架

# 定义乘法测试类，并继承unittest的TestCase类
class Testmul(unittest.TestCase):
    '''乘法测试'''

    # 定义具体的乘法测试方法
    def test_mul1(self):
        m1 = Clac(2, 5)
        self.assertEqual(m1.mul(), 10, 'your calculate is wrong')

    def test_mul2(self):
        m2 = Clac(3, 4)
        self.assertEqual(m2.mul(), 12, 'your calculate is wrong')

if __name__ == '__main__':
    unittest.main()
