#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-08 , 16:38

import requests

url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
response = requests.get(url, data)
print(response.text)

response = requests.post(url, data)
print(response.json())
