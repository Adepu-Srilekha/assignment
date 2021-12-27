#Giving a new name to an existing list is called aliasing

list1=[1,2,3,4,5]
list2=list1
print(list1)
print(list2)

#we can give this way also
list1=[1,2,3,4,5]
list2=list1[:]
print(list1)
print(list2)