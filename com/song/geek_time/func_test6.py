#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/15 , 10:24

fd = open('naem.txt')
try:
    for line in fd:
        print(line)
finally:
    fd.close()

# 不用写finally  with会自动调用finally
with open('naem.txt') as f:
    for line in f:
        print(line)