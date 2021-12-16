#largest number from list
#using in built function
list1=[1,2,3,4,5,6,7,8,9]
print(max(list1))

#finding largest number from list and taking the input dynamically
list2=[]
size=int(input('enter how many numbers you want to enter:'))
print('enter',size,'elements')
for i in range(size):
    data=int(input('enter the numbers:'))
    list2.append(data)
max=0

for data in list1:
    if data>max:
        max=data
print('the largest number is',max)





'''output :
enter how many numbers you want to enter
enter 5 numbers
1
2
3
4
5
'''

