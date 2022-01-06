List1=[]
for i in range(10):
    List1.append(i)
print(List1)
print(List1[::-1])
#print(List1.upper())

list1=['hyderabad','bangalore','delhi']
print('reverse',list1[::-1])
list2=list1[::-1]
print('list2',list2)
list3 = []
for i in list2:
    x = i.upper()
    list3.append(x)
print(list3)
