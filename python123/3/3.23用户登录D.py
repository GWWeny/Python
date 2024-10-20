dic={'admin':'123456','administrator':'12345678','root':'password'}
for i in range(4):
    username=input()
    password=input()
    if username in dic.keys() and password==dic[username]:
        print("登录成功")
        break
    else:
        print("登录失败")