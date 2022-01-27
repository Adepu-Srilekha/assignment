#Compare two arrays and display the resultant boolean type array
from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,4,1])
arr3=arr1==arr2
print('Result of arr1==arr2',arr3)
arr3=arr1>arr2
print('Result of a>b',arr3)
arr3=arr1<=arr2
print('Result of a<=b',arr3)