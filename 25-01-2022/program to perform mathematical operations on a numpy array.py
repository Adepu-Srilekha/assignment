from numpy import *
#creating an array
from numpy import *
arr=array([10,20,30,40,50])
print('original array:',arr)
#arithmatic operations on the elements of the array
print('after adding with 5:',arr+5)
print('after subtracting with 5:',arr-5)
print('after multiplying with 5:',arr*5)
print('after dividing with 5:',arr/5)
print('after modulus with 5:',arr%5)

#we can use the arrays in expressions also
print('Expression value:',(arr+5)**2-10)

#some math functions
print('sin values',sin(arr))
print('cos values',cos(arr))
print('tan values',tan(arr))
print('Biggest element',max(arr))
print('Smallest element',min(arr))
print('sum of all elements:',sum(arr))
print('Average of all elements:',mean(arr))




