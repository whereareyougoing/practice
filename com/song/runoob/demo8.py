#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 2:12 PM

import sys

# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。

def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1

f = fibonacci(100)  # 由生成器生成一个迭代器

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
