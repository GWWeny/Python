#请在...补充代码
import random

def genpwd(length):
    return ''.join(str(random.randint(0,9)) for _ in range(length))
# python123编译不过，跟数据不符合
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
