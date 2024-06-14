#if else
height=int(input("What is yout height?"))
if height>=3:
    print("U can ride")
    age=int(input("Enter your age"))
    if age<18:
        print("Pay 250")
    else:
        print("Pay 500")
else:
    print("Cant ride")
print("BYE")