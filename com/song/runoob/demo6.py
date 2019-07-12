#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 1:19 PM

number = int(input("请输入一个整数："))

if number % 2 == 0:
    if number % 3 == 0:
        print("你输入的数可以整除2和3")
    else:
        print("你输入的数可以整除2不能整除3")
else:
    if number % 3 == 0:
        print("你输入的数不能整除2，可以整除3")
    else:
        print("你输入的数即不能整除2也不能整除3")

