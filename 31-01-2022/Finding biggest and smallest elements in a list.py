'''list1=[1,2,3,4,5]
n1=max(list1)
print(n1)
n2=min(list1)
print(n2)

#the elements in the list are generally represented as list1[i]
big=list1[0]
small=list1[0]
'''
#A python program to find maximum and minimum elements in a list of elements.
x=[]
num=int(input('enter how many elements you want to enter:'))
for i in range(num):
    input1=int(input('enter the number:'))
    x.append(input1)
print('The list is:',x)

#initially 0th element becomes maximum and minimum
big=x[0]
small=x[0]
for i in range(1,num):
    if x[i]>big:big=x[i]
    
    if x[i]<small:small=x[i]
print('maximum is:',big)
print('Minimum is:',small)
