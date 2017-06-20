from calculator20170620 import Count # 从calculator20170620导入Countl类
import unittest # 引入unittest模块

class TestCount(unittest.TestCase): # 创建TestCount继承unittest的TestCase类

    def setUp(self): # 测试用例前的初始化工作
        print('test start')

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5) # 调用unittest框架提供的assertEqual对add()的返回值进行断言

    def tearDown(self): # 与setUp()方法相呼应，用于测试用力执行后的善后工作
        print('test end')

if __name__ == "__main__":
    unittest.main()