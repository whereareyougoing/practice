#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  ${DATE} , ${TIME}

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "from@runoob.com"
receivers = ["songaiheng@126.com"]

message = MIMEText('python 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header('菜鸟教程', 'utf-8') # 发送者
message['To'] = Header('测试', 'utf-8') # 接收者

subject = 'python SMTP 邮件测试'
message[subject] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.send(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('error: 邮件发送失败')


