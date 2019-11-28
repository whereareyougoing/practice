#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/28 , 15:36

import re

p = re.compile('.{3}')
print(p.match('bat'))

# r   标记  表示后面的符号不转译
p1 = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p1.match('2018-05-10').group())
print(p1.match('2018-05-10').groups())
print(p1.match('2018-05-10').group(1))
print(p1.match('2018-05-10').group(2))
print(p1.match('2018-05-10').group(3))

# 搜索功能，不完全匹配，只要包含了正则表达式匹配的规则，就能匹配成功
print(p1.search('aa2018-11-10bb'))

phone = '123-456-789 # 这是一个电话号码'

p2 = re.sub('#.*$', "", phone)
print(p2)

p3 = re.sub(r'\D', '', p2)

print(p3)

# 匹配多次  search只能匹配出第一个
re.findall('')
