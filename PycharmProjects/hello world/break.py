l1=["hi","hello","welcome"]
names=["Ram","Madhav","Bala"]
for item in l1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Madhav":
            break
    print("out from inner loop")
print("out from outer loop")