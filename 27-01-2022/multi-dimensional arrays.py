#Multi=dimensional arrays:

#2D-arrays,3D arrays etc., are called multi dimensional arrays.



#we can create multi dimensional arrays in the following ways:

#1.using array()
from numpy import *
arr1=array([[1,2],[3,4]])
print(arr1)


#2.using ones() and zeros()
'''syntax
a=ones((rows,columns),dtype)'''
a=ones((3,4),int)
print('a:',a)

b=zeros((2,3),float)
print(b)



#3.using eye()
'''creates a 2D array and fills the elements in the diagonal with 1s.
syntax:eye(n,dtype=datatype)
The default datatype is float
'''

a1=eye(3)
print(a1)


#using reshape()
#This function is useful to convert a 1D array to multi dimentsional array.
a=array([1,2,3,4,5,6])
b=reshape(a,(2,3))
print(b)

#3D array
a2=arange(12)
print(a2)
b1=reshape(a2,(3,2,2))
print(b1)
#3 inner arrays
# 2 rows
#2 columns


#A python program to retrieve the elements from a 2D array and display them using forloops

from numpy import *
a=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(a)):
    print(a[i])

#display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end='')









list1=[1,2,3,4,5]
list1.append(40)
list1.extend([1,2,3])