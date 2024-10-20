from random import randrange
import random
n=int(input())
m=int(input())
p=int(input())
random.seed(n)
data = {'user'+str(i):
            {'film'+str(randrange(1,p)) for j in range(randrange(p))} for i in range(m)}
user = {'film1', 'film2', 'film3'}
print(data)
similarUser,films=max(data.items(),key=lambda item:(item[1]!=user,len(item[1]&user)))
# print(data)
views = list(films - user)
print(sorted(views))
