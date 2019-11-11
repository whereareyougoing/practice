#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/11 , 15:24

# 迭代器

list = [1,2,3]
it = iter(list)
print(it.__next__())
print(it.__next__())
print(it.__next__())


# 后面的2 是步长
for i in range(10,20,2):
    print(i)

# 生成器
def frange(start, stop, step):
    x = start
    while x < stop:
        yield (x)
        x += step

for i in frange(10,20,0.5):
    print(i)
