#判断是否是素数
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
    return True
#返回判断是否是素数的函数
def isprime(x):
    return is_prime(x[1])
def getprime(n):
    #生成2到n-1的列表
    numbers =list(range(2,n))
    #enumerate生成数个元组，filter(isprime会过滤掉结果是False的元组，
    #为什么这样，要根据isprime来根据
    seq=filter(isprime,enumerate(numbers,2))
    #x[1] 访问元组的第二个元素（即原始数字），这就是我们要提取的质数值。
    #返回seq中的符合元素
    return [x[1] for x in seq]

x=int(input())
print(getprime(x))
