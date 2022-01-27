#The reshape() method:
#It is useful to change the shape of the array.
#But the new array should have the same number of elements as in thr original array.

from numpy import *
arr1=arange(10)
print(arr1)

#changing the shape
arr1=arr1.reshape(2,5)
print(arr1)


arr1=arr1.reshape(5,2)
print(arr1)



#Flatten() method:
#useful to return a copy of the array collapsed into one dimension.
arr1=array([[1,2,3],[4,5,6]])
print(arr1)

#using flatten() method we can convert this array to 1D array
arr1=arr1.flatten()
print(arr1)
