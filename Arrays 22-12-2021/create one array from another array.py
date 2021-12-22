from array import *
array1=array('f',[1.0,3.9,3.8,4])

#we are using the above array and multiply each element of array1 with 3
#typecode---gives the type code character of the array 'array1'
array2=array(array1.typecode,(a*3 for a in array1))
for i in array2:
    print(i)