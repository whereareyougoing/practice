#! /usr/bin/env python 
# 宋艾衡  2019/7/12 , 11:14 AM

# 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

def bubleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [11, 23, 21, 45, 32, 10, 9]

bubleSort(arr)

print("排序后的数列为：")
print(arr)