n,m=map(int,input().split())
# input().split()：读取一行输入并按空格分隔，返回一个字符串列表。
#  map(int, ...)：将每个字符串转换为整数。
#  n 和 m：分别代表课程数和学生数。
gardes=[]
for _ in range(m):
    line=list(map(float,input().split()))
    gardes.append(line)

average_scores=[]
for i in range(n):
    # 使用列表推导式计算每门课的总分。grades[j][i]
    # 访问第 j 个学生在第 i 门课的成绩。
    total=sum(gardes[j][i] for j in range(m))
    average=total/m
    average_scores.append(average)

for i in average_scores:
    print(i)