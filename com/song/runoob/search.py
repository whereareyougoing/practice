#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 9:26 PM


# 线性查找

def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1

arr = ["a", "b", "c", "d", "e"]

x = "d"

result = search(arr, len(arr), x)

if result != -1:
    print("索引为：", result)
else:
    print("不存在")