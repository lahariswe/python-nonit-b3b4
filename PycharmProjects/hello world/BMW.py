w=float(input("enter the weight in kg"))
h=float(input("enter the height in meter"))
bmw= round(w/h ** 2)
if bmw<18.5:
    print(f"Your BMW is {bmw} and your underweight")
elif bmw<25:
    print(f"Your BMW is {bmw} and your normal weight")
elif bmw<30:
    print(f"Your BMW is {bmw} and your overweight")
elif bmw<35:
    print(f"Your BMW is {bmw} and your Obese")
else:
    print(f"Your BMW is {bmw} and your clinically obese")