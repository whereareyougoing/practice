#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-10-21 , 23:31

alist = []
for i in range(1, 10):
    if i % 2 == 0:
        alist.append(i*i)
print(alist)
print(alist[0])


blist = [i*i for i in range(1, 11) if i % 2 == 0]
print(blist)


zodiac_name = (u'摩羯座',  u'水瓶座',  u'双鱼座',  u'自羊座',  u'金牛座', u'双子座', u'巨覆座', u'狮子座', u'处女座', u'天押座',  u'天蝎座',  u'射手座')
zodiac_days = ((1, 20),  (2, 19),  (3, 21),  (4, 21), (5, 21), (6,  22), (7,  23),  (8, 23),  (9, 23),  (10, 23), (11, 23), (12, 23))
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

print(z_num)

z_num = {i: 0 for i in zodiac_name}
print(z_num)