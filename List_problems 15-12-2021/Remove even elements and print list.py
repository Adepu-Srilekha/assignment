#Remove even elements and print list
list1=[1,2,3,4,5,6]
for even in list1:
    if even %2 == 0:
        print('even numbers in the list',even)
        list1.remove(even)
print('after removing even elements ',list1)