a=eval(input())
if  isinstance(a,dict):
    d={value:key for key,value in a.items()}
    print(d)
else:
    print("输入错误")
