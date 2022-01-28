#sorting the matrix
#synatx:sort(matrixname,axis)
#axis=1......rowwise
#axis=0........column wise
#default value of axis is 1,if do not mention axis value it takes as 1
from numpy import *
m=matrix([[5,3,2],[9,7,6]])
print(m)
#for sorting
a=sort(m)
print('sorting',a)
#column wise
b=sort(m,axis=0)
print('sorting column wise',b)



