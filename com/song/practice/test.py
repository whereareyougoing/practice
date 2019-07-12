#! /usr/bin/env python 
# coding : utf-8
# @Auther : 宋艾衡
# @Date ：2019/1/9 , 12:35 AM

number = 0
while(number < 10):
    print('the num is' ,number)
    number +=1

print('-------------')

number=0
while(number<10):
    number+=1
    if(number%2 > 0):
        continue
    print(number)

print('--------------------')

number=0
while 1:
    print(number)
    number+=1
    if number>5:
        break