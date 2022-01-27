#A python program to copy an array as another array
from numpy import *
a=arange(1,7)
#creating a copy of a
b=a.copy()
print('original array:',a)
print('copy of the array',b)
b[0]=100
print('after modification:')
print('original array:',a)
print('copy of the array',b)
#here by using copy only the modified array...........gives the modified version..

