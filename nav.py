user=int(input("any number"))
user2=int(input("any number"))
user3=int(input("any number"))
if user>user2 and user>user3:
    print("oldest")
elif user2<user and user2<user3:
    print("youngest")
else:
    print("nothing")