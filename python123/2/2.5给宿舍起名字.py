x=[]
for i in range(4):
    name=input()
    x.append(name[-1])
y=''.join(x)
print(f"我们宿舍的组合是：{y}")