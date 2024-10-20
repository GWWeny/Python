x=list(map(int,input().split(",")))
y=list(map(float,input().split(",")))
n=len(x)
sum_x=sum(x)
sum_y=sum(y)
sum_xy=sum([xi * yi for xi,yi in zip(x,y)])
sum_x2=sum([xi ** 2 for xi in x])

b=(n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
a=(sum_y-b*sum_x)/n
total=a+b*(n+1)
print(f"{total:.1f}")