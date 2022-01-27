#A python program to retrieve non zero elements from an array.
from numpy import *
a=array([1,0,3,0,5,0],int)
#it will retrieve indexes of nonzero elements from a
c=nonzero(a)
print(c)

'''for i in c:
    print(i)'''

#To display the elements
print(a[c])