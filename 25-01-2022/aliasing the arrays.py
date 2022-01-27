from numpy import *
#create a with elements 1 to 5
a=arange(1,6)
b=a
print('original array:',a)
print('after aliasing',b)
#modify 0th element of b
b[1]=77
print('after modification',b)

