#smallest number from list
#in built function
list1=[1,2,3,4,5,5,6]
print(min(list1))


size=int(input('enter how many numbers you wanto to give:'))
print('enter',size,'elements')

for i in range(size):
    data=int(input('enter the elements are:'))
    list1.append(data)
    list1.sort()
min_value=list1[0]
for j in list1:
    if list1[j]<min_value:
        min_value=list1[j]
print('small number',min_value)






#using sort function
list1.sort()
print('the smallest number in the list',list1[0])