#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-09-27 , 20:22

import base64
f = open('123.jpeg', 'rb')  #二进制方式打开图文件
ls_f = base64.b64encode(f.read())  #读取文件内容，转换为base64编码
f.close()
print(ls_f)
