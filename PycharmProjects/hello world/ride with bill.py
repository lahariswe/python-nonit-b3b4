height=int(input("What is yout height?"))
bill=0
if height>=3:
    print("U can ride")
    age=int(input("Enter your age"))
    if age<12:
        bill=100
        print("Pay 100")
    elif age<=18:
        bill=250
        print("Pay 250")
    else :
        bill=500
        print("Pay 500")
        want_pic=input("Do you want a photo(y/n)")
        if want_pic=='Y' or want_pic=='y':
            bill=bill+50
            print(f"Your total bill is {bill}")
else:
    print("Cant ride")
print("BYE")