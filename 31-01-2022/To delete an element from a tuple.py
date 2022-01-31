#A program to delete an element from a particular position in the tuple.
num=(1,2,3,4,5)
print(num)
#to accept position number of the element to delete
pos=int(input('Enter position no.'))
#copy from 0th to pos-2 into another tuple num1
num1=num[0:pos-1]


#concatenate the remaining elements of num from pos till end
num=num1+num[pos:]
print(num)
