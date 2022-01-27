#A python program to retrieve and display elements of a numpy array using indexing
from numpy import *
#creating array with elements 10 to 15
a=arange(10,16)
print(a)

#to retrieve from 1st to 6th element in steps of 2
a=a[1:6:2]
print(a)
#to display elements using indexing
i=0
while i<len(a):
    print(a[i])
    i+=1