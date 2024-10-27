from itertools import groupby
import math
from itertools import permutations
# 计算1+2+3+…+100 的值。
s=0
for i in range(1,101):
    s+=i
print(s)
print("1+2+3+...+100=",sum(range(1,101)))
print("="*30)
# 输出序列中的元素
a_list=['a','b','mpligrim','z','example']
for i,v in enumerate(a_list):
    print("列表的第",i+1,"个元素是：",v)
print("="*30)
#  求1~100之间能被7整除，但不能同时被5整除的所有整数
for i in range(1,101):
    if i%7==0 and i%5!=0:
        print(i)
print("="*30)
# 输出所有3位“水仙花数”。所谓n位水仙花数是指1个n位的十进制数，
# 其各位数字的n次方之和等于该数本身。例如：153是水仙花数，因为153 = 13 + 53 + 33 。
for i in range(100,1000): # 法1
    bai,shi,ge=map(int,str(i))
    if bai**3+shi**3+ge**3==i:
        print(i)
for num in range(100, 1000): # 法2
    if sum(map(lambda x:int(x)**3, str(num))) == num:
        print(num)
print("="*30)
# 统计考试成绩中优、良、中、及格、不及格的人数。
scores = [89, 70, 49, 87, 92, 84, 73, 71, 78, 81, 90, 37,
          77, 82, 81, 79, 80, 82, 75, 90, 54, 80, 70, 68, 61]
groups = {'优秀': 0, '良': 0, '中': 0, '及格': 0, '不及格': 0}
def classify(score):
    if score >= 90: return '优秀'
    elif score >= 80: return '良'
    elif score >= 70: return '中'
    elif score >= 60: return '及格'
    else: return '不及格'

groups = {category:len(tuple(score))
          for category, score in groupby(sorted(scores), classify)}
print(groups)
print("="*30)
# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j,end="\t")
    print()
print("="*30)
# 求200以内能被17整除的最大正整数
for i in range(200,1,-1):
    if i%17==0:
        print(i)
        break
print("="*30)
# 判断一个数是否为素数
n = int(input('Input an integer:'))
m = math.ceil(math.sqrt(n)+1)
for i in range(2, m):
    if n%i == 0 and i<n:
        print('No')
        break
else:
    print('Yes')
print("="*30)
# 鸡兔同笼
for ji in range(31):
    if 2*ji + (30 - ji) * 4 == 92:
        print("鸡有",ji,"只，兔子有",30-ji,"只")
        break
print("="*30)
# 编写程序，输出由1、2、3、4这四个数字组成的每位数都不相同的所有三位数。
digits = {1, 2, 3, 4}
for num in permutations(digits, 3):
    num = int(''.join(map(str, num)))
    print(num)
print("="*30)