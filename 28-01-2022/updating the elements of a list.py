list1=list(range(1,5))
print(list1)

#appending
list1.append(7)
print(list1)

#update 1st element of list
list1[1]=8
print(list1)
#updating 1st and 2nd elements of list
list1[1:3]=10,11
print(list1)

#To delete first index
del list1[1]
print(list1)

#removing.. in the removing we pass the element to be removed
list1.remove(7)
print(list1)

