# -*- coding: utf-8 -*-
'''
@author : Ben
练习编写发送带有附件的邮件
'''
import smtplib # 导入smtplib可以发起smtp会话，发送邮件
from email.mime.text import MIMEText # 该模块可以定义邮件主题
from email.mime.multipart import MIMEMultipart

smtpserver = "smtp.gmail.com" # smtp邮箱服务器
username = "xxx@gmail.com" # 发送邮箱账号
password = "xxx" # 发送邮箱密码或授权码
send_mail = "xxx@gmail.com" # 发件人邮箱
receive_mails = ['xxx@163.com', 'xxx@qq.com'] # 接收邮箱数组，可以同时给多个邮箱发送邮件
send_attached  = open('C:\\Users\\Administrator\\Desktop\\csv.csv', 'rb').read() # 发送的文件路径


title = 'python smtplip 带附件邮件测试' # 邮件主题
# 邮件正文是MIMEText:
att = MIMEText(send_attached, 'base64', 'utf-8')
# 添加必要的头信息
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename = "csv.csv"'

# 邮件对象:
msgRoot = MIMEMultipart()
msgRoot['Subject'] = title
msgRoot.attach(att)

try:
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.set_debuglevel(1) # 设置为调试模式，在会话过程中会有输出信息
    smtp.ehlo() # 表明需要用户认证
    smtp.login(username, password)  # 登录验证
    smtp.sendmail(send_mail, receive_mails, msgRoot.as_string())  # 发送邮件
    print("mail has been send successfully.")
    smtp.quit() # 结束smtp会话
except BaseException as error:
    print(error)
