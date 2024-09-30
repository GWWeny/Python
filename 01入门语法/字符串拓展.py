# 单引号定义法，双引号定义法，三引号定义法
name='111'
print(type(name))
name="222"
print(type(name))
name='''333'''
print(type(name))

# 引号嵌套
name='"nihao"'
print(name)
name="'wohenhao"
print(name)
name="\"dajiahenhao\""
print(name)
name='\'yimada\''
print(name)

# 字符串拼接：非字符串类型无法与字符串拼接，使用+来拼接。
name="nige"
print("我的名字是：" + name)

# 字符串格式化：通过占位的方式进行拼接
name="恶龙"
message="公主爱上%s" % name
print(message)

class_num=57
avg_salary=987.5
message="Python大数据学科：深圳%s期，毕业平均工资%f" %(class_num,avg_salary)
print(message)

#精度控制
num=11
num=11.345678323123124534643
print("%4.3f" % num)
print("%4.3d" % num)

# 快速格式化
name="liuzuwei"
year=2004
price=19.99
print(f"我是{name},出生于{year},只有{price}")

# 表达式格式化
print("1*12的结果是%d" % (1*12))

# 数据输入
name=input()
print(f"输入的数据{name},数据类型是{type(name)}")