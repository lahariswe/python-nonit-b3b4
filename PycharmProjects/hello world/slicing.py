num= [10,0,-17,8,88,998]
print(num[0:4])
print(num[0:3])
print(num[:])
print(num[2:4])

#sorting
num.sort()
print(num)#not in mix lists

#reverse
num.reverse()
print(num)

#append(add)
num.append(33)
print(num)

#specific index
num.insert(2,444)
print(num)

#extend
num.extend([444,777,666])
print(num)

#change particular index
num[4]=9999
print(num)

#remove
num.remove(0)
print(num)

#pop last element is removed be default
num.pop()
print(num)

