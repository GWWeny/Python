rp=float(input())
month=int(input())
method=input()
mi=float(input())
if method=="ACPI":
    mra=rp*mi*(1+mi)**month/((1+mi)**month-1)
    print(round(mra,2))
elif method=="AC":
    y=[]
    for i in range(1,month+1):
        mra=rp/month+(rp-(i-1)*rp/month)*mi
        mra=round(mra,2)
        y.append(mra)
    print(f"[{', '.join(map(str,y))}]")
else:
    print("还款方式输入错误")
