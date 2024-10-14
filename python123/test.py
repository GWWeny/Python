from random import randrange
data={'user'+str(i):{'film'+str(randrange(1,10)) for j in range(randrange(1,15))} for i in range(10)}
print(data)
user={'film1','film2','film3'}
similarUser,films=max(data.items(), key=lambda item:(item[1]!=user,len(item[1]&user)))
print(similarUser)
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)

