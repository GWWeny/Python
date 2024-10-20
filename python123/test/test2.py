from random import randrange
data={'user'+str(i):{'filmName'+str(randrange(1,10)):str(randrange(1,5)) for j in range(randrange(1,6))} for i in range(10)}
user={'filmName1':3,'filmName7':4,'filmName5':1}
user_films = set(user.keys())
similarUser,filmNames=max(data.items(), key=lambda item:(item[1].keys!=user.keys(),len(set(item[1].keys()) & user_films)))
print(similarUser)