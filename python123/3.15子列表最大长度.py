def find(lst):
    lens=len(lst)
    maxs=lens
    for i in lst:
        if isinstance(i,list):
            maxs=max(maxs,find(i))
    return maxs
list1=eval(input())
print(find(list1))