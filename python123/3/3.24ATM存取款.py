number1=int(input())
money=1000
if number1==1:
    number2=eval(input())
    if money<number2:
        print("Insufficient Funds")
    elif number2>=100 and number2 %100==0:
        money=money-number2
        print("Balance:"+str(money))
    else:
        print("Incorrect Amount")
elif number1==2:
    number2=eval(input())
    if number2>=100 and number2 %100==0:
        money=money+number2
        print("Balance:"+ str(money))
    else:
        print("Incorrect Amount")
else:
    print("Wrong Option")