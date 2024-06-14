count=5
while count>0:
    print(count)
    count-=1
else:
    print("in else block")
print("out from loop")


count=5
while count>0:
    print(count)
    count-=1
    if count==3:
        break
else:
    print("in else block")
print("out from loop")

number=int(input("enter a number(-q to quit)"))
while number !=-1:
    print(number)
    number=int(input("enter a number(-q to quit)"))
else:
    print("in else block")
print("out of loop")

