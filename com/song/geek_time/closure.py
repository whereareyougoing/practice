#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/11 , 20:53

# 闭包

def func():
    a = 1
    b = 2
    return a+ b
def sum(a):
    def add(b):
        return a+b
    return add
num1 = func()
num2 = sum(2)
print(type(num1))
print(type(num2))
print(num1)
print(num2(4))
# 内部函数引用外部函数值的方式叫做闭包


# 计数器
def counter(first=0):
    cnt = [first]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num5= counter(5)
num10 = counter(10)

print(num5())
print(num5())
print(num5())
print(num10())
print(num10())
print(num10())











