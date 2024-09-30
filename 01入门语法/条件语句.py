# 条件判断语句
# 1
num=19
if num>10:
    print("num>10")
else:
    print("num<10")

# 2
username="leiboyang"
if(username=="leiboyang"):
    print("207色长")
else:
    print("shaniao")

# 3
if(5==5):
    print("true")
print("结束")

# 多条件判断语句
score=input("请输入分数:")
data=int(score)
if(data>90):
    print("甲")
elif(data>80):
    print("乙")
elif(data>70):
    print("丙")
elif(data>60):
    print("丁")
else:
    print("劣")

# 条件嵌套语句
num=input()
if(num=="1"):
    print("话费相关业务")
    print("话费查询请按1；话费充值请按2：")
    num=input()
    if(num=="1"):
        print("话费查询为100元")
    elif(num=="2"):
        print("话费充值50元")
    else:
        print("滚")
elif num=="2":
    print("业务办理")
elif num=="3":
    print("人工服务")
else:
    print("序号输入错误")
