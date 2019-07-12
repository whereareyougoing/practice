#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 4:20 PM

# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

lower = int(input("最小值："))
upper = int(input("最大值："))

for num in range(lower, upper+1):
    sum = 0
    n = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit**n
        temp //= 10
    if num == sum:
        print(num)
