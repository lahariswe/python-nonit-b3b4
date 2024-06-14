size=input("What is the size of the pizza (s/l/m)")
bill=0
if size =='s' or 'S':
    bill=100
    print("The price of the pizza is 100")
elif size == 'm' or 'M':
    bill=200
    print("The price of the pizza is 200")
else: 
    bill=300
    print("The price of the pizza is 300")

add_pepp=input("Do you want to add pepperoni(y/n)")
if add_pepp=='y'or'Y':
    if size =='s' or 'S':
        bill+=30
    else:
        bill+=50

ex_che=input("Do u want extra cheese(y/n)")
if ex_che=='y' or ex_che=='Y':
    bill+=20
print(f"Your total bill is {bill} rupees")



