#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/12 , 17:09

import time

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间为：%s  秒' % (stop_time - start_time))
    return wrapper

# 语法糖，timer是装饰函数，下面的是被装饰函数
@timer
def i_can_sleep():
    time.sleep(3)

#
# start_time = time.time()
#
# 在函数运行的时候timer会将函数作为参数传递进去，
i_can_sleep()
#
# stop_time = time.time()

# 装饰器和闭包的区别是，装饰器传入的是一个函数，内部调用的也是一个函数，
# python的装饰器，和java的注解很像，java的注解也是通过注解的程序来增强原本程序的功能



