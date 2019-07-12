#! /usr/bin/env python 
# 宋艾衡  2019/7/10 , 4:08 PM

list1 = [12, 34, 568, 78, 11]
tup = (12, 33, 22, 11, 34)

print(max(list1))
print(len(list1))
print(min(list1))
print(list(tup))

list1.append(123)
print(list1)
# 统计某个元素出现的次数
a = list1.count(12)
print(a)
list1.index(12)
print(list1)
list1.insert(2, 33)
print(list1)
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1.pop(-1)
print(list1)
# 移除列表中某个值的第一个匹配项
list1.remove(11)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list2 = list1.copy()
print(list2)
list1.clear()
print(list1)

