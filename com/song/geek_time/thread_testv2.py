#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 15:45

import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = MyThread()
t1.start()
t1.join()

print(current_thread().getName(), 'end')
