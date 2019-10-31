#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-10-17 , 23:19

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# for cz in chinese_zodiac:
#     print(cz)

# for year in range(2000, 2019):
#     print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

import time

num = 5
while True:
    print('a')
    time.sleep(1)
    num += 1
    if num > 10:
        break


