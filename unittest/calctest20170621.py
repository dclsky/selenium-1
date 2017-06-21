from calculator20170620 import Count # 从calculator20170620模块导入Count类
import unittest # 导入unittest模块

class TestCount20170621(unittest.TestCase): # 创建TestCount20170621类，继承unittest的TestCase类

    def setUp(self): # 测试用例执行前的初始化工作
        print('test start')

    def test_count1(self):
        a = Count(3,4) # 根据类Count创建对象
        self.assertEqual(a.add(),7) #调用unittest的assertEqual对add()的返回值进行断言

    def test_count2(self):
        b = Count(4,5)
        self.assertEqual(b.add(),9)

    def tearDown(self): # 测试用例执行后的善后工作
        print('test end')

if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite() #调用unittest的TestSuite()类创建测试套件
    suite.addTest(TestCount20170621("test_count1")) #通过addTest()方法添加测试用例
    suite.addTest(TestCount20170621("test_count2"))
    # 执行测试
    runner = unittest.TextTestRunner() # 封装unittest的TextTestRunner()类
    runner.run() # 调用TextTestRunner()类的run()方法来执行测试套件
