#where() function
#---used to create a new array based on whether a given condition is true or not.


#syntax:
#array=where(condition,expression1,expression2)

#if condition is true,expression1 is executed and result is stored into the array...
#else expression2 is executed and result is stored into the array.



from numpy import *
a=array([1,2,3,4,5],int)

b=where(a%2==0,a,0)#for which the condition becomes true then it returns a to that otherwise 0 it returns
print(b)
c=where(a>b,a,b)
print(c)