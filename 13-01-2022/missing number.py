#missing number
'''Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.'''

def missing_number(num_list):
    print(num_list)
    list1=[]
    length=len(num_list)
    for i in range(0,length+1):
        list1.append(i)
    for element in list1:
        if element not in num_list:
            print(element)

size=int(input('enter the length :'))
num_list=[]
for i in range(size):
    element=int(input('enter no:'))
    num_list.append(element)

a=missing_number(num_list)
print(a)

