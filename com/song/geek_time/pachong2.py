#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-08 , 01:50

from urllib import parse
from urllib import request

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')

response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read())

import urllib
import socket

try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
