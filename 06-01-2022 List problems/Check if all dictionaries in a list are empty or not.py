#Check if all dictionaries in a list are empty or not
#list1=[{'a':1,'b':2},{'c':3,'d':4}]
list1=[{'a':1},{},{}]
length=len(list1)
print(length)
count=0
for element in list1:
    if element =={}:
        count+=1
if count==length:
    print('all are empty')
else:
    print('not empty')

#To check items wise
list1=[{'a':1},{},{}]
length=len(list1)
print(length)
for element in list1:
    if element =={}:
        print('no elements are present')
    else:
        print('elements are present')