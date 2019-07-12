#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 9:05 PM

# 二分法排序，是效率非常高的排序算法

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l+(r-l)/2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, (mid - 1), x)
        else:
            return binarySearch(arr, (mid+1), r, x)
    else:
        return -1

arr = [23,44,22,10,23,4,23,22,11,32,54,65,7,7,56,564,23]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("索引为：", result)
else:
    print("元素不存在")