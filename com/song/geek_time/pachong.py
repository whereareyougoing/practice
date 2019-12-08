#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-07 , 23:59

from urllib import request

url = 'http://www.baidu.com'
response = request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))
