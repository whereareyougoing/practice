#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 4:14 PM

for i in range(1, 10):
    for j in range(1, i+1):
        print("{} x {} = {}\t".format(j, i, i*j), end=' ')
    print()