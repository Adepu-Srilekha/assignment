#syntax:
#arrayname[start:stop:slicing]
from array import*
x=array('i',[1,2,3,4,5,6])
y=x[1:2]
print(y)
y=x[-1:]
print(y)
y=x[:4]
print(y)
y=x[-4:-1]
print(y)