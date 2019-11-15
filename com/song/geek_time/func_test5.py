#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/15 , 10:09

# 定义有参数的装饰器
def new_tips(argv):
    def tips(func):
        def nei(a,b):
            # __name__  获得方法的名称
            print('start %s %s' % (argv,func.__name__))
            # 给装饰器的方法加参数
            func(a,b)
            print('stop')
        return nei
    return tips

@new_tips('add')
def add(a,b):
    print(a+b)

@new_tips('sub')
def sub(a,b):
    print(a-b)

print(add(4,5))
print(sub(7,3))