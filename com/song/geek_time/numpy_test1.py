#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-04 , 00:29

import numpy as np

arr4 = np.arange(10)

arr4[5:8] = 10


arr_slis = arr4[5:8].copy()

arr_slis[:] = 15

print(arr_slis)

print(arr4)