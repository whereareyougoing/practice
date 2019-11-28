#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/28 , 16:39

import time
import datetime

# 1970年到现在的秒数
print(time.time())

# 现在年月日时间和秒数
print(time.localtime())

print(time.strftime('%y-%m-%d', time.localtime()))

print(datetime.datetime.now())

newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

one_day = datetime.datetime(2000, 5, 27)
newdate = datetime.timedelta(days=10)
print(one_day+newdate)
