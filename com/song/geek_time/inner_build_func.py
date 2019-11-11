#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/11 , 16:22

from functools import reduce
# Python的一些内建函数
# filter 按照函数条件进行过滤，python3使用filter又使用lambda需要进行类型强制转换
a = [1,2,3,4,5,6]
print(list(filter(lambda x:x>2, a)))
# map对元素进行依次处理
a = [1,2,3,4,5,6]
print(list(map(lambda x:x+1,a)))
# 传入两个参数的map，问？集合相加的结果是什么样的，和sql的取合是否一样
b = [4,5,6]
print(list(map(lambda x,y:x+y,a,b)))
# reduce  使用前先导入模块,  让一堆元素进行叠加操作
print(reduce(lambda x,y:x+y , [2,3,4],1))
# zip 混合元组
for i in zip((1,2,3),(4,5,6)):
    print(i)
dicta = {'a':'aa', 'b':'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))

