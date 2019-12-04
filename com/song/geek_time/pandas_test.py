#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-04 , 22:22

from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 5, 6, -7])

print(obj)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])

print(obj2)

obj2['c'] = 6

print(obj2)

print('f' in obj2)

# 字典直接转换成series ,  key  直接转换成索引，value  直接转换成值
sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000}
obj3 = Series(sdata)
print(obj3)

obj3.index = ['a', 'b', 'c', 'd']
print(obj3)

data = {'city': ['shangahi', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# 直接将多维数组转换成DataFrame
frame = DataFrame(data)
# 直接输出一个二维的数组
print(frame)

# 把DataFrame进行排序, columns后面的字段是排序优先参考的顺序
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

print(frame2)

# 转换一维数组输出
print(frame2['city'])
print(frame2.year)

# 赋值新的一列，将一列全部赋值
frame2['new'] = 100
print(frame2)

frame2['cap'] = frame2.city == 'beijing'
print(frame2)


pop = { 'beijing':{2008:1.5,2009:2.0},
        'shanghai':{2008:2.0,2009:3.6}
        }

frame3 = DataFrame(pop)

print(frame3)
# 行列互换
print(frame3.T)

# 重置索引
obj4 = Series([4.5,7.2,-5.3,3.5],index=['b','d','c','a'])
obj5 = obj4.reindex(['a','b','c','d','e'],fill_value=0)
# 空值会影响数据的清洗，将空值重新填充
print(obj5)

obj6 = Series(['blue','purple','yellow'],index=[0,2,4])
# 对缺失的值进行填充
print(obj6.reindex(range(6),method='bfill'))

from numpy import nan as NA

# 直接将缺失的值删除
data = Series([1,NA,2])

print(data.dropna())


data2 = DataFrame([[1.1,6.5,3],[1,NA,NA],[NA,NA,NA]])
print(data2)
# 删除整行的值为缺失值
print(data2.dropna(axis=1,how='all'))

data2.fillna(0)
print(data2.fillna(0,inplace=True))
print(data2)


import numpy as np

# 多维索引，可以将数据更好的进行分类
data3 = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])

print(data3['b':'c'])

# 将数组转换成1维，    将数组转换成2维
print(data3.unstack().stack())









