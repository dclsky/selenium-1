# -*- coding: utf-8 -*-
'''
@author : Ben
将登录和注册测试用例组装成测试套件，并在执行测试后自动生成测试报告
'''
import unittest,time
from HTMLTestRunner import HTMLTestRunner

# 指定测试用例文件夹，并将该文件夹中的文件组装成测试套件
test_dir = "./"
suite = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

# 格式化获取当前时间
now = time.strftime("%Y%M%d_%H%M%S")

# 定义测试报告存放路径和名称
filename ='C:\\Users\\Administrator\\Desktop\\' + now + 'result.html'
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner(stream=fp,
                        title=u"phpwind测试",
                        description=u"测试登录和注册")

# 执行测试，并在结束后关闭测试报告
runner.run(suite)
fp.close()