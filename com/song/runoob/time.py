#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/7/15 , 10:47

import time

localtime = time.localtime(time.time())
print("本地时间:", localtime)


# 获取格式化的时间
localtime1 = time.asctime(localtime)
print("格式化之后的本地时间：", localtime1)

# 使用 time 模块的 strftime 方法来格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))