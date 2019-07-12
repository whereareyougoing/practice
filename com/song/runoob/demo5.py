#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 11:27 AM

import random
import string

# 猜字游戏

numbers = random.sample(range(0, 100), 1)
number = numbers[0]
guess = -1

while number != guess:
    guess = int(input("请输入数字:"))

    if guess == number:
        print("恭喜你，猜对了！！")
    elif guess < number:
        print("小了")
    elif guess > number:
        print("大了")
