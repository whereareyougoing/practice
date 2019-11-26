#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 17:31

import re

# 被匹配的
p = re.compile('a')
# 匹配任意一个字符
p1 = re.compile('.')
# 匹配任意三个字符
p2 = re.compile('...')
# 匹配所有以jpg结尾的字符
p3 = re.compile('jpg$')
# 前边的一个字符出现0次或者多次
p4 = re.compile('ca*t')
# 前边的一个字符出现1次或者多次
p5 = re.compile('ca+t')
# 前边的一个字符出现0次或1次
p6 = re.compile('ca?t')
# 前边的一个字符出现4次
p7 = re.compile('ca{4}t')
# 前边的一个字符出现4-6次
p8 = re.compile('ca{4,6}t')
# 配置前面是c后面是t中间是bcd其中一个的
p9 = re.compile('c[bcd]t')
#  |  和分组  ()  配合使用

#  ^  以什么开头  以c开头
#  或者是取反 '[^a-z]' 所有小写字母之外的字符
# '[^a-zA-Z]' 所有大写和小写字母之外的字符
# '[^0-9]' 所有数字之外的字符
p11 = re.compile('^c')

# 转义字符
# /d == [0-9]+  匹配多个数字
# /D
# /s  匹配字符串

# 正则分组  ()    .group

# 正则组合
# ^$ 这行没有字符

# .*?  不使用贪婪模式   只用第一个出现的  .  匹配的内容


# 要匹配
print(p.match('a'))
print(p.match('b'))
