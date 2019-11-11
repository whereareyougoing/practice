#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/11 , 16:00


def true():
    return True

res0 = lambda :True
print(res0())

def add(x,y):
    return x+y
print(add(1,2))

res = lambda x,y : x+y
print(res(1,3))

def func(sex):
    if sex == '男':
        return '带把的'
    else:
        return '仙女降世'


res1 = lambda sex:'带把的' if sex == '男' else '仙女降世'
print(res1('女'))