#slicing operations on arrays
from numpy import *
a=arange(1,8)
print(a)
#to receive 1 to 6 element in steps of 2
b=a[1:6:2]
print(b)

#to retrive all elements from a
b=a[::]
print(b)

#to retrieve all elements in reverse order
b=a[::-1]
print(b)

b=a[-2:2:-1]
print('decreasing step size:',b)
#from 0 index value to -2 value index
b=a[:-2:]
print('decreasing:',b)