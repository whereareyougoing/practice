#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 10:37 AM

# 斐波那契数列

# 斐波那契数列的应用，F1**2 + F2**2 + F3**2 + ....+ Fn**2 = Fn**2 * F(n+1)**2  F为每个小正方形的边长

a, b = 0, 1

while b < 1000:
    print(b, end=',')
    a, b = b, a+b
