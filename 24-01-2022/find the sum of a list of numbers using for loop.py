#A python program to display and find the sum of a list of numbers using for loop.

#initially creating a dynamic list

size=int(input('enter the size of the list:'))
list1=[]
for i in range(size):
    input1=int(input('enter numbers:'))
    list1.append(input1)
print(list1)
sum =0
for j in list1:
    sum+=j
print(sum)