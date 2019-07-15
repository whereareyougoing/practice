#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/7/15 , 10:33

import json

data1 = {
    "no": 123,
    "name": "runoob",
    "url": "www.runoob.com"
}

# 写入
json_str = json.dumps(data1)
print("原始数据：", json_str)

# 读取
data2 = json.load(json_str)
print("解析后的数据：", data2["name"])