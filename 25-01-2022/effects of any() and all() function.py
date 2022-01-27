from numpy import *
a=array([1,2,3,4,8])
b=array([7,8,9,4,5])

c=a>b
print('Result of a>b',c)
print('check if any one element is True:',any(c))
print('To check all the elements all true:',all(c))
if all(a>b):
    print('a contains atleast one element greater than those of b')