#! /usr/bin/env python
# 宋艾衡  2019/7/9 , 9:16 PM


# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
#
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
str = 'runoob'

print(str)
print(str[0])
print(str[0:-1])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + "test")


# List（列表） 是 Python 中使用最频繁的数据类型。
#
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
#   python 的 list 可以放不同类型的任意元素

list = ['123',2.4,34,'runoob']
list1 = ['123','runoob']

print(list)
print(list[0:3])
print(list[2:])
print(list[0:-1])
print(list * 2)
print(list + list1)

# 元组  Tuple  类似java的数组，初始化之后大小不能被改变，但是和java的数组不一样的是，java的数据里只能存放同一类型的元素
# go语言中的数组类型也不能够改变，初始化可以不声明数组的长度，但是go会根据初始数据的长度自动初始化数组的长度

tuple = ('123',12.3,34,"runoob",3.12)
tuple1 = (345,"wer",12.3)

print(tuple)
print(tuple[0])
print(tuple[0:])
print(tuple[0:4])
print(tuple[1:-1])
print(tuple + tuple1)
print(tuple * 2)

#  集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#
# 基本功能是进行成员关系测试和删除重复元素。
#
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
#   集合的成员类型需要一致，这里的set集合和java里的set集合类似

student = {"jim", "tom", "tony", "jack", "rose"}

if "rose" in student:
    print(student)

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b) # 两个集合的差集
print(a | b) # 两个集合的并集
print(a & b) # 两个集合的交集
print(a ^ b) # 两个集合不同时存在的元素

# 字典数据类型

dict = {}
dict["one"] = "菜鸟教程"
dict[1] = "cainiaojiaocheng"

tinydict = {"name": "菜鸟教程", "code": "1", "site": "www.runoon.com"}

print(dict["one"])
print(dict[1])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
