#union operation
set1={'RAM','SHYAM','BALA'}
set2={'BALA','JIYA','AAKASH'}
set3={'PRADEEP','ANKUR'}
print(set1.union(set2))
print(set1 |set2)#method
print(set1 |set2| set3)
print(set1.union(set2,set3))

#difference
print(set1-set2)
print(set1.difference(set2))

#intersection
print(set1.intersection(set2))

#


