#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 15:26


class Testwith():
    # 类的初始化调用
    def __enter__(self):
        print('run')
    # 类的结束调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常借宿')
        else:
            print('有异常 %s' %exc_tb)


with Testwith():
    print('with is running')
    raise NameError('name error')