# 下面的代码用来计算小于100的最大素数，注意break语句和else子句的用法。
for n in range(100,1,-1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
        break
# 删除上面代码中最后一个break语句，则可以用来输出100以内的所有素数。