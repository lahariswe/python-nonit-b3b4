name='JAYANTI'
for i in name:
    print(i)

names=["RAM","BALA","SAI"]
for j in names:
    print(j)
    if j=='SAI':
        print("exists")
    else:
        print("Doesnt exists")

l4=[2,3,4,-5,10]
for k in l4:
    square=k**2
    print(square)

l1=[2,3,4,-5,10]
squares=[]
for k in l1:
    square=k**2
    squares.append(square)
print(f"The list of squares is {squares}")
