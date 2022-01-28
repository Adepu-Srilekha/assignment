#Transpose of a matrix
#syntax:t=m.transpose()


#creating a matrix of 3x3 size
from numpy import *
m=matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
#to tranpose
t=m.transpose()
print(t)
#we can also find tranpose using getT()
t1=m.getT()

print('t1',t1)