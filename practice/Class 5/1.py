# Python中的函数和自定义对象的成员也是可以随时发生改变的，
# 可以为函数和自定义对象动态增加新成员
def func():
    print(func.x)
func.x=3
func()
print(func.x)
del func.x # 删除
# func() 删除之后不可访问

# 普通参数
def demo(a,b,c):
    print(a,b,c)
demo(7,6,9) # 形参与实参需一致

# 默认值参数
# 调用带有默认值参数的函数时，
# 可以不对默认值参数进行赋值，也可以为其赋值，具有很大的灵活性
def say(message,times=3):
    print(message*times)
say("干你娘")
def join(lst,sep=None):
    return (sep or'').join(lst)
aList=['a','b','c']
print(join(aList))
print(join(aList,','))
# 默认值参数必须出现在函数参数列表的最右端，
# 任何一个默认值参数右边不能有非默认值参数
# def func(a,b=6,c):
 #   print(a,b,c)

def demo(newitem, old_list=None):
    if old_list is None:
        old_list= []
    new_list=old_list[:]
    new_list.append(newitem)
    return new_list
# 默认值参数的赋值只会在函数定义时被解释一次。
# 当使用可变序列作为参数默认值时，一定要谨慎操作
print(demo('5', [1,2,3,4]))
print(demo('aaa', ['a','b']))
print(demo('a'))
print(demo('b'))

# 通过关键参数，实参顺序可以和形参顺序不一致，
# 但不影响传递结果，避免了用户需要牢记位置参数顺序的麻烦
def demo1(a,b,c=5):
    print(a,b,c)
demo1(3,7)
demo1(c=7,b=3,a=6)

# 可变长度参数主要有两种形式：在参数名前加1个星号*或2个星号**。
# *parameter用来接收多个位置实参并将其放在元组中，元组长度由实际接收到的实参数量确定。
# **parameter用来接收多个关键参数并存放到字典中，字典长度由实际接收到的实参数量确定。
def demo2(*p):
    print(p)
demo2(1,2,3,4,5,6,7,)
def demo3(**p):
    for item in p.items():
        print(item)
demo3(x=1,y=2,z=3)

# 几种不同类型的参数可以混合使用，但是不建议这样做
def func_4(a, b, c=4, *aa, **bb):
    print(a, b, c)
    print(aa)
    print(bb)

func_4(1, 2, 3, 4, 5, 6, 7, 8, 9, xx='1', yy='2', zz=3)

