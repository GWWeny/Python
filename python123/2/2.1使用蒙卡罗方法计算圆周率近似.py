import random
sd = int(input())
n = int(input())
# sd作为种子
random.seed(sd)
c=0
for i in range(n):
    x,y=random.uniform(-1,1),random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        c+=1
a = c/n*4
print(f"{a}")