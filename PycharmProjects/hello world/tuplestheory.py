tuple1=(12.0,-9,"Sai",True)
print(tuple1)
print(tuple1[2])
print(tuple1[-1])
#print(tuple1[6])
print(type(tuple1))

tuple2=(45)
print(type(tuple2))

tuple3=(45,)
print(type(tuple3))

#they are immutable(non changeable)
#tuple1[1]=13
#jprint(tuple1)

#dulpicate items are allowed
tuple4=(12,12,6,6)
print(tuple4)
#slicing is possible
print(tuple4[1:])

#length
print(len(tuple4))

#nesting of tuples
tuple5=(tuple4+tuple1)
print(tuple5)#concatenation#len is no. of elements
          #0    #1
tuple5=(tuple4,tuple1)
print(tuple5)
print(tuple5[0])
print(tuple5[1])
print(len(tuple5))#2

print(min(tuple4))#cannot take place in mixed
print(max(tuple4))

print(tuple4.count(12))
print(tuple4.index(12))

#conv of list to tuple
list1=[1,45,98,77]
print(tuple(list1))

tuple6=(10,)*5
print(tuple6)

