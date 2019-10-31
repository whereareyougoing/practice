#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-10-17 ,  23:32

zodiac_name = (u'摩羯座',  u'水瓶座',  u'双鱼座',  u'自羊座',  u'金牛座', u'双子座', u'巨覆座', u'狮子座', u'处女座', u'天押座',  u'天蝎座',  u'射手座')
zodiac_days = ((1, 20),  (2, 19),  (3, 21),  (4, 21), (5, 21), (6,  22), (7,  23),  (8, 23),  (9, 23),  (10, 23), (11, 23), (12, 23))

# 用户输入int类型的日期
int_mouth = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))

# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_mouth, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_mouth == 12 and int_day >= 23:
#         print(zodiac_name[0])
#         break

n = 0
while zodiac_days[n] < (int_mouth, int_day):
    if int_mouth == 12 and int_day > 23:
        break
    n += 1
print(zodiac_name[n])