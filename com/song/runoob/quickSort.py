#! /usr/bin/env python 
# 宋艾衡  2019/7/12 , 10:58 AM



# 快速排序的基本思想就是从一个数组中任意挑选一个元素（通常来说会选择最左边的元素）作为中轴元素，
# 将剩下的元素以中轴元素作为比较的标准，将小于等于中轴元素的放到中轴元素的左边，将大于中轴元素的放到中轴元素的右边。

# 然后以当前中轴元素的位置为界，将左半部分子数组和右半部分子数组看成两个新的数组，
# 重复上述操作，直到子数组的元素个数小于等于1（因为一个元素的数组必定是有序的）。

#  快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
#
# 步骤为：
#
#     挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
#     分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。
# 在这个分割结束之后，对基准值的排序就已经完成;
#     递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
#
# 递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
#
# 选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。

def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i], end=' ')

