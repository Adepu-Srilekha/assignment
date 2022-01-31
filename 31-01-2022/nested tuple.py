#Nested tuple:
#A tuple inserted inside another tuple is called nested tuple.
tup=(1,2,3,4,5,6,7,(3,5))
print(tup[0])
print(tup[7])

#A python program to sort a tuple with nested tuples.
emp=((20,'srilekha',2000.30),(10,'Niharika',5000.40),(30,'Ameena',9000.70))
print(sorted(emp))#sorts by default on id
print(sorted(emp,reverse=True))#sorts reverse on id
print(sorted(emp,key=lambda x:x[1])) #sort on name
print(sorted(emp,key=lambda x:x[2])) #sort on salary

