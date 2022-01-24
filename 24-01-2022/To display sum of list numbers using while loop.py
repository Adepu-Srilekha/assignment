size=int(input('enter the size of the list:'))
list1=[]
for i in range(size):
    input1=int(input('enter numbers:'))
    list1.append(input1)
print(list1)
i=0
sum=0
while i<len(list1):
    sum+=list1[i]
    i+=1
print('sum',sum)
