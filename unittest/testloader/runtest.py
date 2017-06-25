# 通过defaultTestLoader类的discover()方法查找制定目录下所有测试模块
import unittest

# 定义测试用例目录为当前目录
test_dir = './'
suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)