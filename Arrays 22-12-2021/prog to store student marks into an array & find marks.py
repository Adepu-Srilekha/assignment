from array import *
#to accept marks from keyboard into a list
list1=[int(i) for i in input('enter marks:').split(',')]
#creating an integer array of marks
marks= array('i',list1)
#to find total
sum=0
for x in marks:
    print(x)
    sum+=x
print('total marks are:',sum)

#to display percentage
#percentage=total marks or sum(marks)/total number of subjects
n=len(marks) #no.of elements in marks  array
percent =sum/n
print('percentage is:',percent)