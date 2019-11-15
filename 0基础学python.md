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