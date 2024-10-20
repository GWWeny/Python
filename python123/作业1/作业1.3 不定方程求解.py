a,b,c=map(int,input().split())
count=0
ls=[]
for x in range(c//a+1):
    for y in range((c-a*x)//b+1):
        if a*x+b*y==c:
            count+=1
            ls.append([x,y])

print(ls)
print(count)