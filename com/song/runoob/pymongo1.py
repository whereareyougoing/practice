#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019/7/15 , 11:12

import pymongo

# 创建mongo数据库
myclient = pymongo.mongo_client("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]

# 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。

# 判断数据库是否已经存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
  print("数据库已存在！")

# 创建一个集合
mycol = mydb["sites"]

# 判断集合是否已经存在
collist = mydb. list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("集合已存在！")



