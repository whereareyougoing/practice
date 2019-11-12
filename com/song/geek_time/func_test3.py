#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/12 , 16:50

def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y


# a = 3 b = 5  定义了一条直线
# x = 10 y = ?

line1 = a_line(3,5)
print(line1(10))
print(line1(20))


# a = 5 b = 10
line2 = a_line(5,10)
print(line2(10))
print(line2(20))







