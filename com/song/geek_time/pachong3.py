#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-08 , 15:31


from urllib import request
from urllib import parse

url = 'http://httpbin.org'

headers = {}

dict = {'name': 'value'}

data = bytes(parse.urlencode(dict), encoding='utf-8')

req = request.Request(url=url, data=data, headers=headers, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))
