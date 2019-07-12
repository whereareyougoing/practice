#! /usr/bin/env python 
# 宋艾衡  2019/7/11 , 2:00 PM


# 声明成迭代器类，需要实现两个方法
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x, end=' ')


