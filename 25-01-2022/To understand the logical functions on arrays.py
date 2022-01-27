from numpy import *
a=array([1,2,3,4,5],int)
b=array([0,8,3,5,4])
c=logical_and(a>0,a<4)
print(c)

c=logical_or(b>=0,b==1)
print(c)

c=logical_not(b)
print(c)