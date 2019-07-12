#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 11:18 AM

# python中 大于0的整数都是true，0 是false

age = int(input("请输入狗狗的年龄:"))
if age < 0:
    print("傻屌，你在扯淡吗？")
elif age == 1:
    print("相当于人类的年龄 14 岁")
elif age == 2:
    print("相当于人类的年龄 22 岁")
elif age > 2:
    human = 22 + (age-2) * 5
    print("相当于人类的年龄：", human)

# 退出
input("点击回车退出")