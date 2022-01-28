#products of elements
#syntax:
#m=matrix(arange(12).reshape(3,4))

from numpy import *
m=matrix(arange(12).reshape(4,3))
print(m)
#to find the prod of elements
a=m.prod(0)
print(a)

#to find the prod of elements row wise
b=m.prod(1)
print(b)