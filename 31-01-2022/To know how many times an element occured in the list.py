#A python program to know how many times an element occured in the list.
x=[]
num=int(input('enter how many elements you want to enter:'))
for i in range(num):
    input1=int(input('Enter elements:'))
    x.append(input1)
print('The list is:',x)
y=int(input('enter the element to count:'))
c=0
for i in x:
    if (y==i):
        c+=1
print('{} is found {} times'.format(y,c))