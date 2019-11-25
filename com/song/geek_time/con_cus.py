#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/11/25 , 15:55

from threading import Thread, current_thread
import time
import random
from queue import Queue

# 定义一个队列
queue = Queue(5)


class ProduceThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' % (name, t))


class Consumer(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            # 封装好了线程等待的方法
            queue.task_done()
            print('消费者 %s 消费了数据 %s ' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 消耗了 %s 秒' % (name, t))

# 生产者多于消费者的时候，会有一段时间生产者不生产数据，因为队列满了
p1 = ProduceThread(name='p1')
p1.start()
p2 = ProduceThread(name='p2')
p2.start()
p3 = ProduceThread(name='p3')
p3.start()
c1 = Consumer(name='c1')
c1.start()
c2 = Consumer(name='c2')
c2.start()