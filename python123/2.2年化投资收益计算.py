x=input()
a=list(map(float,x.split()))
if a[2]==1:
    x=[(a[3]/a[0])/a[1]*1]
elif a[2]==2:
    x=[(a[3]/a[0])/a[1]*12]
elif a[2]==3:
    x=[(a[3]/a[0])/a[1]*365]
print(f"在投资金额为:{a[0]},投资时长为{a[1]},收益为:{a[3]}的情况下,年化收益率为:{x[0]:.3f}")