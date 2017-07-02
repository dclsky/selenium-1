# -*- coding: utf-8 -*-
'''
@author : Ben
获取最新的测试报告
'''
import os

# 定义文件目录
dir = r'C:\Users\Administrator\Desktop\report'
# 将目录内文件组成一个lists,os.listdir()可以获取目录下所有文件和文件夹
lists = os.listdir(dir)
# 按时间给lists内的list排序
lists.sort(key=lambda fn: os.path.getatime(dir + "\\" + fn))
print("最新的报告为："+lists[-1])
file = os.path.join(dir, lists[-1])
print(file)