year =int(input("Enter the Year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("is Leap Year")