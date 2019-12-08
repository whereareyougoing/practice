#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-08 , 16:45

import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

# print(content)

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))
