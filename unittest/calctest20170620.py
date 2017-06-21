from calculator20170620 import Count # 从calculator20170620导入Countl类
import unittest # 引入unittest模块

class TestCount(unittest.TestCase): # 创建TestCount继承unittest的TestCase类

    def setUp(self): # 测试用例前的初始化工作
        print('test start')

    def test_add(self):
        j = Count(2,3) # 根据类Count创建对象j
        self.assertEqual(j.add(),5) # 调用unittest框架提供的assertEqual对add()的返回值进行断言

    def tearDown(self): # 与setUp()方法相呼应，用于测试用力执行后的善后工作
        print('test end')

if __name__ == "__main__":
    unittest.main()
# __name__作为模块的内置属性，就是.py的调用方式；.py有两种调用方式：作为模块被调用和直接使用
# 如果__name__等于__main__就表示直接使用