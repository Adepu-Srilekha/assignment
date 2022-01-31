#Tuples:(Is a sequence which stores a group of elements or items)
#once we create tuple, we cannot modify its elements.
#Hence we cannot perform operations like append(),extend(),insert() etc.,
#similar to lists but the main difference is lists are immutable.

tup1=()#empty tuple
tup2=(10,)#we need to put , if there is only one element
tup3=(1,2,-9,'bangalore',9.0)#with any data type
tup4=(10,20,30) #with integers
tup5=1,2,3#without braces,also becomes tuple

#converting the list to tuple
list1=[1,2,3,4]
tuple1=tuple(list1)
print('tuple',tuple1)

#creating a tuple with range function
tuple2=tuple(range(1,10,2))
print('tuple2',tuple2)


#repetition
tpl=(1,2,3)
tpl2=tpl*2
print('tpl2',tpl2)



#functions to process tuples:
len()
min()
max()
count()
index()
sorted()