#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/8 , 21:46

# 关键字参数，可以不按照顺序传入参数

def func (a,b,c):
    print('a = %s' %a)
    print('b = %s' %b)
    print('c = %s' %c)

func(1 ,c = 3, b =2)


# 可变长参数
def howlong(first, *other):
    print(1+len(other))

howlong(123,234,456)


var1 = 123
def func1():
    global var1
    var1 = 456
    print(var1)

func1()
print(var1)


