def demo():
    global x
    x = 3
    y = 4
    print(x, y)
x=5
demo()
print(x)
# del x
# print(x)

x = 3
def f():
    # print(x)           #本意是先输出全局变量x的值，但是不允许这样做
    x = 5              #有赋值操作，因此在整个作用域内x都是局部变量
    print(x)
# 如果局部变量与全局变量具有相同的名字，
# 那么该局部变量会在自己的作用域内隐藏同名的全局变量

# map()
print(list(map(str,range(5))))
def add5(v):
    return v+5
print(list(map(add5,range(10))))

def add(x, y):return x+y
print(list(map(add, range(5), range(5))))

# reduce()
from functools import  reduce
seq=[1,2,3,4,5,6,7,8,9]
print(reduce(lambda x,y:x+y,seq))
def add(x,y):
    return x+y
print(reduce(add,range(10)))

# lambda表达式只可以包含一个表达式
f = lambda x,y,z:x+y+z
print(f(1,2,3))
g=lambda g,y=2,z=3:g+y+z
print(g(10))
print(g(2,z=4,y=5))
def demo5(n):
    return n**2
print(demo5(5))
a_List=[1,2,3,4,5]
print(list(map(lambda x:demo5(x),a_List)))

import random
x=[[random.randint(1,10) for j in range(5)] for i in range(5)]
y=sorted(x,key=lambda item:(item[1],item[4]))
for item in y:
    print(item)
