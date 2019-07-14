#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-07-14 , 16:32


import _thread
import time

# 为线程定义一个函数
def print_time(threadname, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s:" % (threadname, time.ctime(time.time())))

# 创建两个线程

try:
    _thread.start_new_thread(print_time, ("thread-1", 2))
    _thread.start_new_thread(print_time, ("thread-2", 4))
except:
    print("error: 无法启动线程")

while 1:
    pass