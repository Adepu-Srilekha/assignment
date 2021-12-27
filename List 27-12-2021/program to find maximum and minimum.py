list1=[]
n=int(input('enter how many numbers you want to enter:'))
for i in range(n):
    print('enter element:')
    list1.append(int(input()))
print('the list is:',list1)
big=list1[0]
small=list1[0]
for i in range(1,n):
    if list1[i]>big:
        big=list1[i]
        if list1[i]<small:
            small=list1[i]


print('max is',big)
print('min is:',small)
