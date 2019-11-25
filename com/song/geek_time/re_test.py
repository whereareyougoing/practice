#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 17:31

import re

# 被匹配的
p = re.compile('a')

# 要匹配
print(p.match('a'))
print(p.match('b'))

