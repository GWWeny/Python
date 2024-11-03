#请在...补充代码
import random

def genpwd(length):
    return ''.join(str(random.randint(0,9)) for _ in range(length))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
