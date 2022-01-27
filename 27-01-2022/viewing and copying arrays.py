#To create a view of an existing array
from numpy import *
a=arange(1,6)
print(a)
#creating a view
b=a.view()
print('original array',a)
print('new array:',b)
b[3]=11
print('After modification:')
print('The original array:',a)
print('modified array:',b)
#in the output if we modify b.. a also modifies