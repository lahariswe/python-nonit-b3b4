set1={12,-9,0.987,"RAM",True}
print(set1)

set2={12,-9,0.987,"RAM",True,12,1}
print(set2)
#print(set2[2])err
print(type(set2))

#to create empty set wrong way
set3={}
print(type(set3))

#to create empty set
set4=set()
print(type(set4))

#not to change
#set1[1]=0
#print(set1)
#but can modify the entire set

#add new value to set
set1.add(99)
print(set1)
print(len(set1))
#add an entire tuple
set1.add((333,444,555))
print(set1)

#remove any item
set1.remove(-9)
print(set1)

#key error
#set1.remove(999)
#print(set1)

#discard
set1.discard(12)
print(set1)
set1.discard(999)
print(set1)#shows no error

#pop
#set1.pop()#removes any random element
#print(set1)=