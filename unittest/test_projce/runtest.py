import unittest

test_dir = "./test_case" # 定义工作目录为当前目录下的test_case文件夹
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*test.py") #调用discover()方法查找测试用例并组成测试套件

# 执行用例
runner = unittest.TextTestRunner()
runner.run(discover)