from functools import *
list1=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,list1)
print(result)