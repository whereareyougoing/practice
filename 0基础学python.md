
# 目录 

[toc]

# 1、 Python的语言特点

* python的介绍和封装
* python基本的数据结构

![课程大纲](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/087A94576AD7416DA6D1ADBCA48363CA/11662)

![python语言特点](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/77BA643A67904E9DBEEABC1C41037501/11667)

~~~
    对于新手特别友好，学习曲线小
~~~

# 2、python的历史

> python版本

~~~    
python的发行版
~~~

* 学习python的网站

![学习python的网站](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/B311F6089D2E437C8D7924EB7A3BDE75/11676 '学习python的网站')

# 3、python的安装

# 4、python的书写规则

- 变量赋值，变量命名，命名规范

> 一般很少用_ 来命名，因为下划线是特殊文件的命名开头，驼峰命名方法。

```
    # 注释
    import  导入
    
    缩进，python的结尾是没有分号进行分割的，所以下一行接上上一行的时候需要缩进。
    
```


# 5、基础数据类型

```
        整数，浮点数，布尔，字符串
        
        类型转换，强制类型转换
        
        bool  进行布尔值的转换，非0的就是true
```

# 6、变量的定义和常用操作

```
        变量可以多次进行赋值
        变量命名：
        大小写命名：bandWidth
        驼峰命名：BandWidth
        下划线分割命名：band_width  
        这些命名方式都是合法的
        
        下划线开头的命名也是合法的，但是以下划线开头的一般都是系统的问阿金命名
```


# 7、序列的概念

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/8A2581E6C8C346FDAB8DC1C93FEE8576/11863)

> 字符串

```
    str 可以使用 [n] 单个指针获取当个位置上的值
    可以使用[n:m] 获取范围的值
    也可以使用 [-1] 从队列尾部获取值
```

_**python把所有的数据都看作对象，python没有变量这个概念，只有指针这个概念，变量可以被看作是<br>指针变量**_


# 8、字符串的定义和使用

> 序列的切片操作

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/9F37F68A68994050AF5ADF9CB8557085/11878)

# 9、字符串的常用操作

```
    连接操纵，重复操作
    +   *3  
```

# 10、元组定义和操作

```
    为了避免汉字乱码，可以在字符串的汉字前面加上一个小写的 u
    注：元组类似于java的数组
    元组的数据不能修改，可以添加和删除
    
    元组里数据的类型可以不一致，这个是和java数据有明显的区别的
    
    创建元组时元组里只有一个元素的时候需要在元素后面加一个逗号  temp={a,}
    
    元组的嵌套
    
```

_**python里任何类型都是可以比较的，只要是类型相同**_  &nbsp;&nbsp;&nbsp; 例：(1,20) > (2,20) 

不可变更的数据建议声明成元组，如果是可以变更的建议声明成列表


# 11、列表的定义和操作

```
    列表：[abc,bcd]
    可以增加和删减数据
```
```python
    

```

# 12、条件语句




# 13、for循环

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/F8B5A553502F46D3832CCCC139DDCAC6/12033)

# while语句

# 15、for循环中if语句的嵌套

# 16、 while循环和if嵌套

# 17、字典的定义和常用的操作

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/77D45019D51B441BBF13213643250D54/12045)

` 字典类似于java中的map `

字典值初始化：dic = {}

```python

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 宋艾衡  2019-10-17 ,  23:32

zodiac_name = (u'摩羯座',  u'水瓶座',  u'双鱼座',  u'自羊座',  u'金牛座', u'双子座', u'巨覆座', u'狮子座', u'处女座', u'天押座',  u'天蝎座',  u'射手座')
zodiac_days = ((1, 20),  (2, 19),  (3, 21),  (4, 21), (5, 21), (6,  22), (7,  23),  (8, 23),  (9, 23),  (10, 23), (11, 23), (12, 23))
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0


while True:

    # 用户输入int类型的日期
    year = int(input('请输入年份：'))
    mouth = int(input('请输入月份：'))
    day = int(input('请输入日期：'))

    n = 0
    while zodiac_days[n] < (mouth, day):
        if mouth == 12 and day > 23:
            break
        n += 1
    # 输出生肖和星座
    print(zodiac_name[n])

    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    # 输出生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))


```

# 18、列表推导式与字典推导式
```python
alist = []
for i in range(1, 10):
    if i % 2 == 0:
        alist.append(i*i)
print(alist)
print(alist[0])


blist = [i*i for i in range(1, 11) if i % 2 == 0]
print(blist)


zodiac_name = (u'摩羯座',  u'水瓶座',  u'双鱼座',  u'自羊座',  u'金牛座', u'双子座', u'巨覆座', u'狮子座', u'处女座', u'天押座',  u'天蝎座',  u'射手座')
zodiac_days = ((1, 20),  (2, 19),  (3, 21),  (4, 21), (5, 21), (6,  22), (7,  23),  (8, 23),  (9, 23),  (10, 23), (11, 23), (12, 23))
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

print(z_num)

z_num = {i: 0 for i in zodiac_name}
print(z_num)
    
```

# 19、文件操作
![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/6BFFD162D5634FBE87718C50AB3CD353/12122)


# 20、文件的常用操作

# 21、异常操作

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/201A459987CD4904B4CADCCDC2CF5393/12143)

# 22、函数的定义和常用操作

![](https://note.youdao.com/yws/public/resource/fc0842c41604dbdfeb5b59ea989535e3/xmlnote/275038E9AD384AE4A0E45CC6CED1BAAB/12150)


# 22、函数的定义和常用操作

![图片.png](https://i.loli.net/2019/11/08/mdIcZMLh8ECn5tw.png)



# 23、可变长参数

python自带的函数 python的内置函数

关键字参数调用:关键字参数不用按照参数顺序传入





```python
# 关键字参数，可以不按照顺序传入参数

def func (a,b,c):
    print('a = %s' %a)
    print('b = %s' %b)
    print('c = %s' %c)

func(1 ,c = 3, b =2)


# 可变长参数
def howlong(first, *other):
    print(1+len(other))

howlong(123,234,456)
```



# 24、函数变量的作用域

内部的变量重新定义之后会把外部的变量覆盖

函数内部定义的变量只作用域函数内部

可以在变量上加   global  让局部变量成为全局变量




# 22、函数的定义和常用操作

![图片](https://user-images.githubusercontent.com/17619355/68912540-64be4700-0793-11ea-9734-a6a697b7d726.png)



# 23、可变长参数

python自带的函数 python的内置函数

关键字参数调用:关键字参数不用按照参数顺序传入





~~~python
# 关键字参数，可以不按照顺序传入参数

def func (a,b,c):
    print('a = %s' %a)
    print('b = %s' %b)
    print('c = %s' %c)

func(1 ,c = 3, b =2)


# 可变长参数
def howlong(first, *other):
    print(1+len(other))

howlong(123,234,456)
~~~



# 24、函数变量的作用域

内部的变量重新定义之后会把外部的变量覆盖

函数内部定义的变量只作用域函数内部

可以在变量上加   global  让局部变量成为全局变量



# 25、函数迭代器与生成器

迭代器

生成器：带有yield的迭代器



```python
# 生成器  yield 的作用是运行到这个位置才会输出
def frange(start, stop, step):
    x = start
    while x < stop:
        yield (x)
        x += step
```

​	

# 26、lambda表达式

```python
def true():
    return True

res0 = lambda :True
print(res0())

def add(x,y):
    return x+y
print(add(1,2))

res = lambda x,y : x+y
print(res(1,3))

def func(sex):
    if sex == '男':
        return '带把的'
    else:
        return '仙女降世'


res1 = lambda sex:'带把的' if sex == '男' else '仙女降世'
print(res1('女'))
```

lambda只能简化简单的逻辑，复杂的逻辑还是需要正常的代码方式去实现



# 27、python的内建函数



```python
from functools import reduce
# Python的一些内建函数
# filter 按照函数条件进行过滤，python3使用filter又使用lambda需要进行类型强制转换
a = [1,2,3,4,5,6]
print(list(filter(lambda x:x>2, a)))
# map对元素进行依次处理
a = [1,2,3,4,5,6]
print(list(map(lambda x:x+1,a)))
# 传入两个参数的map，问？集合相加的结果是什么样的，和sql的取合是否一样
b = [4,5,6]
print(list(map(lambda x,y:x+y,a,b)))
# reduce  使用前先导入模块,  让一堆元素进行叠加操作
print(reduce(lambda x,y:x+y , [2,3,4],1))
# zip 混合数组
for i in zip((1,2,3),(4,5,6)):
    print(i)
# 调换k，v位置
dicta = {'a':'aa', 'b':'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))
```



# 28、闭包的定义

```python
# 闭包

def func():
    a = 1
    b = 2
    return a+ b
def sum(a):
    def add(b):
        return a+b
    # 闭包返回外部函数的返回值的时候，返回内部函数的名称
    return add
num1 = func()
num2 = sum(2)
print(type(num1))
print(type(num2))
print(num1)
print(num2(4))
# 内部函数引用外部函数值的方式叫做闭包
```

```python
# 计数器
def counter(first=0):
    cnt = [first]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num5= counter(5)
num10 = counter(10)

print(num5())
print(num5())
print(num5())
print(num10())
print(num10())
print(num10())
```



# 29、闭包的应用

```python

# 闭包解决了在a，b  不变的情况下  x改变，带来的y改变的问题，如果使用普通的函数，需要定义三个值
# 即便a b  不变爱是需要每次都传值

def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y

# a = 3 b = 5  定义了一条直线
# x = 10 y = ?

line1 = a_line(3,5)
print(line1(10))
print(line1(20))


# a = 5 b = 10
line2 = a_line(5,10)
print(line2(10))
print(line2(20))
```



# 30、装饰器

```python

import time

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间为：%s  秒' % (stop_time - start_time))
    return wrapper

# 语法糖，timer是装饰函数，下面的是被装饰函数
@timer
def i_can_sleep():
    time.sleep(3)

#
# start_time = time.time()
#
# 在函数运行的时候timer会将函数作为参数传递进去，
i_can_sleep()
#
# stop_time = time.time()

# 装饰器和闭包的区别是，装饰器传入的是一个函数，内部调用的也是一个函数，
# python的装饰器，和java的注解很像，java的注解也是通过注解的程序来增强原本程序的功能
```



# 31、装饰器的使用

```python
# 定义有参数的装饰器
def new_tips(argv):
    def tips(func):
        def nei(a,b):
            # __name__  获得方法的名称
            print('start %s %s' % (argv,func.__name__))
            # 给装饰器的方法加参数
            func(a,b)
            print('stop')
        return nei
    return tips

@new_tips('add')
def add(a,b):
    print(a+b)

@new_tips('sub')
def sub(a,b):
    print(a-b)

print(add(4,5))
print(sub(7,3))
```



# 32、自定义上下文管理

![图片](https://user-images.githubusercontent.com/17619355/68912311-cb8f3080-0792-11ea-8683-2130850f9ac3.png)



# 33、模块的定义

![图片](https://user-images.githubusercontent.com/17619355/69050842-ca356080-0a3d-11ea-8a40-1f2fbb3ea9bd.png)





# 34、pep 8编码规范



# 35、类和实例

```python

# 面向对象编程

class Player():
    def __init__(self, name, hp):  # 构造方法
        self.name = name
        self.hp = hp

    def print_role(self):  # 自定义一个方法
        print('%s : %s' %(self.name, self.hp))


user1 = Player('zhangsan', 100) # 类的实例化
user2 = Player('lisi', 120)

user1.print_role()
user2.print_role()
```

面向过程更适合机器运行，面向对象更符合人的思维习惯



# 36、如何增加类的属性和方法

```python
class Player():
    def __init__(self, name, hp, occu):  # 构造方法
        self.__name = name  # 变量被称为属性   两个下滑线对类进行封装，类似于java的private
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 自定义一个方法
        print('%s : %s' %(self.__name, self.hp))


    def updateName(self,newname):
        self.__name = newname


class Monster():
    '定义怪物类'
    pass   # 类不报错



user1 = Player('zhangsan', 100, 'war') # 类的实例化
user2 = Player('lisi', 120, 'master')


user1.print_role()
user1.updateName('walson')
user1.print_role()
user2.print_role()
```



# 37、类的集成

python的面向对象和java有异曲同工的特点，<br>所有的面向对象都符合面向对象的三大特性，封装，集成，多态



# 38、类的使用-自定义with

```python
class Testwith():
    # 类的初始化调用
    def __enter__(self):
        print('run')
    # 类的结束调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常借宿')
        else:
            print('有异常 %s' %exc_tb)


with Testwith():
    print('with is running')
    raise NameError('name error')
```



# 39、多线程编程的定义

* 并发编程

  例子：收银台收银，多收银台收银，就是并发解决问题

* 多线程编程：

  ```python
  
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
  ```

  

# 40、经典的生产者和消费者问题

	> 水槽问题：一边防水，一边注水，数据一边生产一边消耗

* 队列

  先进先出，先放进去的先读取

多线程并发的写入和读取

消息处理：使用队列处理消息，队列满了会开启一个新的线程，处理消息，避免消息的积压

```python

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
```



# 41、python标准库的定义

python的官方库，www.python.org

常用的库：

+ 文字处理 re
+ 日期类型  time   datetime
+ 数字和数学类型    math   random
+ 文件和目录访问   pathlib    os.path
+ 数据压缩存档   tarfile
+ 多线程    threading   queue
+ 通用操作系统   os   logging   argparse
+ Internet数据处理   base64   json   usllib
+ 结构化标记处理工具   html  xml
+ 开发工具   untiltest
+ 调试工具   timeit
+ 软件包发布   venv
+ 运行服务   _main_



# 42、正则表达式库



# 43、正则表达式的元字符

