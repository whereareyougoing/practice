#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 4:57 PM

with open("text.txt", "wt") as out_file:
    out_file.write("该文本会写入文件中\n看到我了吧")

with open("text.txt", "rt") as in_file:
    text = in_file.read()

print(text)