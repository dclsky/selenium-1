# -*- coding: utf-8 -*-
'''
@author : Ben
练习编写发送不带附件的邮件
'''
import smtplib # 导入smtplib可以发起smtp会话，发送邮件
from email.mime.text import MIMEText # 该模块可以定义邮件主题
from email.header import Header # 该模块可以定义邮件正文

smtpserver = "smtp.gmail.com" # smtp邮箱服务器
username = "xxx@gmail.com" # 发送邮箱账号
password = "xxx" # 发送邮箱密码或授权码
send_mail = "xxx@gmail.com" # 发件人邮箱
receive_mails = ['xxx@163.com', 'xxx@qq.com'] # 接收邮箱数组，可以同时给多个邮箱发送邮件

# 纯文本格式邮件测试
title = 'python smtplip 纯文本邮件测试' # 邮件主题
content = '这是由python smtplib给你发送的一封邮件' # 纯文本格式的邮件正文
msg = MIMEText(content, 'plain', 'utf-8') # 正文，格式(plain为纯文本格式)，编码
'''构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8编码保证多语言兼容性'''
msg['Subject'] = Header(title, 'utf-8') # 定义邮件主题

# html格式邮件测试
# title = 'python smtplip html邮件测试' # 邮件主题
# content = '<html><hl>你好！</hl></html>' # html格式的邮件正文
# msg = MIMEText(content, 'html', 'utf-8') # 正文，格式(html格式)，编码
# '''构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8编码保证多语言兼容性'''
# msg['Subject'] = Header(title, 'utf-8') # 定义邮件主题

try:
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.set_debuglevel(1) # 设置为调试模式，在会话过程中会有输出信息
    smtp.ehlo() # 表明需要用户认证
    smtp.login(username, password)  # 登录验证
    smtp.sendmail(send_mail, receive_mails, msg.as_string())  # 发送邮件
    print("mail has been send successfully.")
    smtp.quit() # 结束smtp会话
except BaseException as error:
    print(error)
