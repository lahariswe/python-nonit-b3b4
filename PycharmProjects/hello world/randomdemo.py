import random as rd

a=rd.randint(1,3)
print(a)
#1<=x>=3

a=rd.randrange(1,3)
print(a)
#1<=x>3

a=rd.random()
print(a)
#3998.736

a=rd.uniform(1,3)
print(a)
#2.987654
#1.098655

l=[90,0,-1,8,88]
a=rd.choice(l)
print(a)
#90#-1

l=[90,0,-1,8,88]
rd.shuffle(l)
print(l)
#shuffling

