from calc import Clac # 从calc模块中导入Clac类
import unittest # 导入单元测试框架

# 定义加法测试类，并继承unittest的TestCase类
class Testadd(unittest.TestCase):
    '''加法测试'''

    # 定义具体的加法测试方法，注意这里需要以‘test’开头
    # 因为unittest的main()方法使用TestLoader类来搜索该模块中的测试方法，只能搜索以‘test’开头的测试方法
    def test_add1(self):
        a1 = Clac(1, 2)
        self.assertEqual(a1.add(), 3, 'your calculate is wrong')

    def test_add2(self):
        a2 = Clac(3, 4)
        self.assertEqual(a2.add(), 7, 'your calculate is wrong')

if __name__ == '__main__':
    unittest.main()
# __name__作为模块的内置属性，就是.py的调用方式；.py有两种调用方式：作为模块被调用和直接使用
# 如果__name__等于__main__就表示直接使用
