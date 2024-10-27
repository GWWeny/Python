from itertools import count
from itertools import combinations
from itertools import groupby
import math
# 3-14  有一箱苹果， 4 个 4 个地数最后余下 1 个，
# 5 个 5 个地数最后余下 2 个， 9 个 9 个地数最后余下 7 个。
# 编写程序计算这箱苹果至少有多少个。
for num in count(16,9):
    if num%5 == 2:
        break
for result in count(num,45):
    if result%4==1:
        break
print(result)
print("="*30)
# 编写程序，计算组合数C(n,i)，即从n个元素中任选i个，有多少种选法。
def Cni2(n,i):
    return int(math.factorial(n)/math.factorial(i)/math.factorial(n-i))
print(Cni2(6,2))
print("="*30)
# 根据字符种类数量判断密码安全强度
def rules(ch):
    if '0'<=ch<='9':return 'digits'
    if 'a'<=ch<='z': return 'lowercase'
    if 'A'<=ch<='Z': return 'uppercase'
    if ch in ',._': return 'punctrations'
def check(pwd):
    grade = {1: 'weak', 2: 'below middle', 3: 'above middle', 4: 'strong'}
    num=len(tuple(groupby(sorted(pwd),key=rules)))
    return grade.get(num,'not suitable')
print(check('abcd'))
print(check('A,'))
print(check('Abcd1234,'))
print("="*30)
# 编写程序，计算理财产品收益，假设收益和本金一起滚动
def licai(base,rate,days):
    result=base# 初始投资金额
    times=365//days # 一年可以滚多少期
    for i in range(times):
        result+=result*rate/365*days
    return result
print(licai(100000,0.0385,14))
print("="*30)
# 验证6174猜想。1955年，卡普耶卡(D.R.Kaprekar)对4位数字进行了研究，
# 发现一个规律：对任意各位数字不相同的4位数，使用各位数字能组成的最大数减去能组成的最小数，
# 对得到的差重复这个操作，最终会得到6174这个数字，并且这个操作最多不会超过7次
digits=list(range(10))
found=False
for item in combinations(digits,4):
    if len(set(item))==4:
        times=0
        current=int((''.join(map(str,item))))
        seen=set() # 记录已出现的差值，避免无限循环
        while current!=6174:
            times=times+1
            big=int(''.join(sorted(str(current),reverse=True)))
            little=int(''.join(sorted(str(current))))
            difference=big-little
            if difference in seen: # 避免出现重复差值，退出循环
                break
            seen.add(difference)
            current=difference # 更新current为新计算的差值
            if current==6174:
                print(item,':',times)
                found = True
if not found:
    print("没有组合能达到6174")
