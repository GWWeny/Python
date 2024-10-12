matrix=eval(input())
print(len(matrix))# 矩阵列
print(len(matrix[0]))# 矩阵行
#用列表推导式实现行列互换，错误代码为：new= [[row[i] for row in matrix] ]
#修改后正确代码为
new = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(new)