#attributes of an array:


#The ndim Attribute:


#The ndim attributes represents the number of dimensions or axes of the array
#number of dimensions is also referred as 'rank'.
from numpy import *
arr1=array([1,2,4,5,])#1D array
print(arr1.ndim)


arr2=array([[1,2,3],[4,5,6]])
print(arr2.ndim)



#The shape attribute:
#gives the shape of the array
#The shape is a tuple listing the number of elements along each dimension.
arr3=array([1,2,3,4,5])
print('shape',arr3.shape)

arr4=array([[1,2,3],[4,5,6]])#2 rows and 3 columns
print('arr4 shape',arr4.shape)

#changing the shape to 3 rows and 2 columns
arr4.shape=(3,2)
print(arr4)







#The size attribute:
#It gives the total number of elements in the array.
arr5=array([1,2,3,4,5])
print('size',arr5.size)

arr6=array([[1,2,3,4,5],[8,9,6,5,2]])
print('size1',arr6.size)






#The itemsize attribute:
#It gives the memory size of the array elements in bytes.
arr7=array([1,2,3,4,5])
print('itemsize',arr7.itemsize)


arr8=array([1.0,2.0,3.0,4.0,5.0])
print('item size of float',arr8.itemsize)




#The dtype attribute:
#It gives the datatype of the elements in the array.
arr9=array([1.0,2.0,3.0,4.0,5.0])
print('datatype',arr9.dtype)

arr10=array([1,2,3,4,5])
print('datatype',arr10.dtype)





#The nbytes attribute:
#It gives the total no.of bytes occupied by an array
#Total number of bytes=size of the array*item size of each element
arr11=array([[1,2,3],[4,5,6]])
print('nbytes',arr11.nbytes)






