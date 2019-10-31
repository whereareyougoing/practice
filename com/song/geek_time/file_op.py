#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-10-22 , 00:05

# file1 = open('naem.txt','w')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('naem.txt')
# var1 = file2.read()
# file2.close()
# print(var1)
#
# file3 = open('naem','a')
# file3.write('刘备')
# file3.close()

file4 = open('naem.txt')
print(file4.readline())

file5 = open('naem.txt')
for i in file5.readlines():
    print(i)
    print('********')

file6 = open('naem.txt')
# 指针的概念
print(file6.tell())
file6.read(1)
print(file6.tell())
file6.seek(0)
print(file6.tell())
print(file6.tell())
# 0 从文件开头进行偏移，1 从当前的位置进行偏移，2 从结尾进行偏移
file6.seek(5,0)
print(file6.tell())
file6.seek(5,1)
print(file6.tell())
file6.close()