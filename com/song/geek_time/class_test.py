#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019-11-19 , 00:04


# 自定义一个类

# 面向对象编程，把对象汇聚在一起，把公共的东西进行提取

#
# 面向过程编程
#
# def print_role(rolename):
#     print('name is %s ' % (rolename['name'], rolename['hp']))


class Player():
    def __init__(self, name, hp, occu):  # 构造方法
        self.__name = name  # 变量被称为属性   两个下滑线对类进行封装，类似于java的private
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 自定义一个方法
        print('%s : %s' % (self.__name, self.hp))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到一个位置')

    def ask(self):
        print('我是一个怪物')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'boss怪'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def ask(self):
        print('我是大boss')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
print(type(a1))

a2 = Animals(12)
print(a2.hp)
print(a2.run())
print(type(a2))

a3 = Boss()
print(a3.hp)
print(a3.ask())
print(type(a3))

print(isinstance(a3, Monster))
print(isinstance(a1, object))

# 所有类的父类是   object


# user1 = Player('zhangsan', 100, 'war')  # 类的实例化
# user2 = Player('lisi', 120, 'master')
#
# user1.print_role()
# user1.updateName('walson')
# user1.print_role()
# user2.print_role()
