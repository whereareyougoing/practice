#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-07-14 , 15:32

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方 SMTP服务
mail_host = "smtp.xxx.com" # 设置服务器
mail_user = "XXX" # 用户
mail_pass = "xxxxxx" # 密码

sender = "from@runoob.com"
receivers = ['songaiheng@126.com'] # 接收邮件

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")