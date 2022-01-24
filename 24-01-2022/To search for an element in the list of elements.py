list1=[1,2,3,4,5,6,7]
search=int(input('Enter the element to search:'))
for element in list1:
    if search==element:
        print('element found in list1')
        break #come out of for loop
else:
    print('element is not found')