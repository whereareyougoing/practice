#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/8 , 21:13

import re

def find_item( hero ):
    with open('sanguo.txt',encoding='GB18030') as f:
        data = f.read().replace('/n','')
        # 词在数据里出现的次数，re为一个函数
        name_num = re.findall(hero,data)
        print('主角 %s 次' %(hero, len(name_num)))
    return len(name_num)

# 读取人物信息
name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

# 排序
name_sort = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sort[0:10])