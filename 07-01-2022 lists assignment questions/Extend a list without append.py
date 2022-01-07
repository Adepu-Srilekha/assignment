#Extend a list without append
list1=[1,2,3,4,5,6]
print('using another variable')
list2=[3,4,5]
list3=(1,2,3,4)
list1.extend(list3)
print(list1)
list1.extend([6,7,8])
print(list1)