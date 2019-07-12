#! /usr/bin/env python 
# 宋艾衡  2019/7/12 , 11:02 AM

import sys

# 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，
# 存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

A = [12, 34, 21, 33, 22, 11, 16]

for i in range(len(A)):

    mid_index = i
    for j in range(i+1, len(A)):
        if A[mid_index] > A[j]:
            mid_index = j

        A[i], A[mid_index] = A[mid_index], A[i]


print("排序后的数列为：")
for i in range(len(A)):
    print("%d" %A[i], end=' ')