#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-11-08 , 18:23



# ValueError  是需要捕获的异常类型

# try:
#     year = int(input('year input:'))
# except ValueError:
#     print('年份需要输入数字')




# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能做除数 %s' % e)
#
#
# # 捕获所有的异常 Exception
# try:
#     print(1/'a')
# except Exception as e:
#     print('出现异常 %s' % e)


# 自定义的错误信息
# try:
#     raise NameError('hello error')
# except NameError as e:
#     print('name error')

try:
    a = open('naem.txt')
except Exception as e:
    print(e)
finally:
    a.close()