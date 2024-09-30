username=input()
key=input()
user_data={
    "aaa":"123456",
    "bbb":"888888",
    "ccc":"333333",
}
if username not in user_data:
    print("Wrong User")
elif key==user_data[username]:
    print("Success")
else:
    print("Fail")
