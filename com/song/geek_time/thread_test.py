#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 15:35

import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    time.sleep(1)
    print('%s %s' % (arg1, arg2))


for i in range(1, 6, 1):
    t1 = myThread(i, i + 1)

for i in range(1, 6, 1):
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()

print(current_thread().getName(),'end')
