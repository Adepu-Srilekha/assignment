'''creating arrays in numpy can be done in several ways:
array()
linspace()
logspace()
arange()
zeros() and ones()'''


#creating integer array using array():
from numpy import*
arr=array([1,2,3,4,5],int)
print(arr)

#creating float array using array():
arr2=array([1.9,8.0,5.7],float)
print(arr2)



#creating array with unicode characters
arr1=array(['a','b','c','d'],)
print(arr1)