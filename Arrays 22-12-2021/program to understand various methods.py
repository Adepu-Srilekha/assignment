from array import *
x=array('i',[1,2,3,4,5])
print('the original array is:',x)
#if we want add element
x.append(6)
print('after appending:',x)
#if we want to remove an element
x.remove(5)
print('after removing :',x)
#if we want to insert 9 at the position 3
x.insert(3,9)
print('after inserting:',x)
#to remove last element we use pop
n=x.pop()
print('after pop:',n)
#to find position using index
n=x.index(4)
print('after using index',n)

#to convert an array to list---- using tolist() method
list1=x.tolist()
print('the converted list is:',list1)
print('the array is:',x)