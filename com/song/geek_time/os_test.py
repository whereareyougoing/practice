#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/12/3 , 17:27

import os

# 当前目录的绝对路径
print(os.path.abspath('.'))
# 上一级的绝对路径
print(os.path.abspath('..'))
# 目录是否存在
print(os.path.exists('/Users'))
# 是否是文件
print(os.path.isfile('/Users'))
# 是否是目录
print(os.path.isdir('/Users'))
# 连接目录
os.path.join('/tmp/a', 'b/c')

from pathlib import Path

p = Path('.')
print(p.resolve())
print(p.is_dir())
# 新建目录
q = Path('./a/b/c')
# 多级目录自动创创建
Path.mkdir(q, parents=True)
