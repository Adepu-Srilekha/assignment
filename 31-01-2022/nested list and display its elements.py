#to create a Nested list and display its elements
#A list within another list is called a nested list.
a=[10,20]
b=[1,2,3,4,a]
print(b)
'''for i in b:
    print(i)'''
#to get nested list :
for i in b[4]:
    print(i)
