# 假设已有若干用户名字及其喜欢的电影清单，现有某用户，
# 已看过并喜欢一些电影，现在想找个新电影看看，又不知道看什么好。
from random import randrange
data={'user'+str(i):{'filmName'+str(randrange(1,10)) for j in range(randrange(15))}
                     for i in range(10)}
user = {'filmname1','filmname2','filmname3'}
similarUser,films=max(data.items(), key=lambda item:(item[1]!=user,len(item[1]&user)))
print("历史数据：")
for u,f in data.items():
    print(u,f,sep=':')
print("和你最相似的用户是",similarUser)
print('Ta最喜欢看的电影是',films)
print("你还没有看过的电影是",films-user)
print("="*30)
# 书评选取
comments = ['这是一本非常好的书，作者用心了',
            '作者大大辛苦了',
            '好书，感谢作者提供了这么多的好案例',
            '书在运输的路上破损了，我好悲伤。。。',
            '为啥我买的书上有菜汤。。。。',
            '啊啊啊啊啊啊，我怎么才发现这么好的书啊，相见恨晚',
            '书的质量有问题啊，怎么会开胶呢？？？？？？',
            '好好好好好好好好好好好',
            '好难啊看不懂好难啊看不懂好难啊看不懂',
            '书的内容很充实',
            '你的书上好多代码啊，不过想想也是，编程的书嘛，肯定代码多一些',
            '书很不错!!一级棒!!买书就上当当，正版，价格又实惠，让人放心!!! ',
            '无意中来到你小铺就淘到心意的宝贝，心情不错! ',
            '送给朋友的、很不错',
            '这是一本好书，讲解内容深入浅出又清晰明了，推荐给所有喜欢阅读的朋友同好们。']
rule= lambda s:len(set(s))/len(s)>0.5
result=filter(rule,comments)
print("原始书评")
for comment in comments:
    print(comment)
print('='*30)
print("经过筛选的书评")
for comment in result:
    print(comment)
    print("="*30)
# 使用最小二乘法计算回归直线
t=(1,2,3,4,5)
y=(5,6,7,8,10)
n=len(t)
t_ave=sum(t)/n
y_ave=sum(y)/n
ly=sum(map(lambda x,y:x*y,t,y))-n*t_ave*y_ave
lt=sum(map(lambda x:x**2,t))-n*t_ave**2
k=round(ly/lt,3) # 直线斜率
b=round(y_ave-k*t_ave,3) # 直线截距
print(k,b)
distance=sum(map(lambda x,y:abs(k*x+b-y),t,y))
distance=round(distance,3)
print(distance)
print(round(6*k+b,3))
print("="*30)