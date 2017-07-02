from calc import Clac # 从calc模块中导入Clac类
import unittest # 导入单元测试框架

# 定义除法测试类，并继承unittest的TestCase类
class Testdiv(unittest.TestCase):
    '''除法测试'''

    # 定义具体的除法测试方法
    def test_div1(self):
        d1 = Clac(5, 2)
        self.assertEqual(d1.div(), 2.5, 'your calculate is wrong')

    def test_div2(self):
        d2 = Clac(6, 3)
        self.assertEqual(d2.div(), 2.0, 'your calculate is wrong')

if __name__ == '__main__':
    unittest.main()
