from itertools import combinations_with_replacement
import itertools
from string import digits

# itertools模块中的函数combinations_with_replacement()可以返回带重复值的组合
primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)
for item in combinations_with_replacement(primes,3):
    if sum(map(lambda x:x**2,item))==2019:
        print(item)
print("="*30)
# itertools还提供了排列函数permutations()。
for item in itertools.permutations(range(1,4), 2):
    print(item)
print("="*30)
# itertools还提供了用于循环遍历可迭代对象元素的函数cycle()。
x='Private Key'
y=itertools.cycle(x)
for i in range(20):
    print(next(y),end='')
print()
print("="*30)
# itertools还提供了根据一个序列的值对另一个序列进行过滤的函数compress()
x = range(1, 20)
y = (1,0)*9 + (1,)
print(y)
print(list(itertools.compress(x, y)))
print("="*30)
# itertools还提供了根据函数返回值对序列进行分组的函数groupby()
def group(v):
    if v > 10:
        return 'greater than 10'
    elif v < 5:
        return 'less than 5'
    else:
        return 'between 5 and 10'
x=range(20)
y=itertools.groupby(x,group)
for k,v in y:
    print(k,':',list(v))
print("="*30)