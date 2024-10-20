# 返回一个元组，排序将首先基于绝对值，其次基于原值
def sort(x):
    return (abs(x),x)
list1=eval(input())
# sorted() 函数对 list1 进行排序。它使用 sort 函数作为 key，根据返回的元组进行排序。
# 因为设置了 reverse=True，所以结果将按降序排列。
list=sorted(list1,key=sort,reverse=True)
print(','.join(map(str,list)))