# 通过unittest框架的defaultTestLoader类来组织测试用例套件
import unittest # 导入unittest框架
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os

# 定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login('xxx@gmail.com','xxx')
    smtp.sendmail('xxx@gmail.com', 'xxx@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out!')

# 在测试报告目录找到最新的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = '.\\'
    test_report = 'C:\\Users\\Administrator\\Desktop\\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py') # 查找当前目录下所有以test开头的.py文件并组成一个测试套件

    now = time.strftime("%Y%m%d_%H%M%S")
    report = test_report + now + 'calcreport.html'
    fp = open(report, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title = "计算器测试报告",
                            description = "test")
    runner.run(discover)
    fp.close()

    now_report = new_report(test_report)
    send_mail(now_report)