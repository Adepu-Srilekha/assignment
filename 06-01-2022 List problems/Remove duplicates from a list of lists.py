list1=[{'a':1},{},{}]
length=len(list1)
print(length)
for element in list1:
    if element =={}:
        print('no elements are present')
    else:
        print('elements are present')