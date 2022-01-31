#List Comprehensions
#To create a list with squares of integers from 1 to 10.
#using for loop without list comprehensions

'''squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)'''


#using list comprehension
squares=[x**2 for x in range(1,11)]
print(squares)

#we want only  squares of integers from 1 to 10 and take only the even numbers from the result
even_squares1=[x**2 for x in range(1,11) if x%2==0]
print(even_squares1)

#without using if statement
even_squares2=[x**2 for x in range(2,11,2)]
print(even_squares2)


#adding two lists
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=[]
for x in list1:
    for y in list2:
        list3.append(x+y)
print('list3',list3)#here the first element is adding with all the other elements of list2

list1=[1,2,3,4]
list2=[5,6,7,8]
list4=list1+list2
print(list4)

#adding the lists using list comprehensions
lst=[i+j for i in [1,2,3,4] for j in [5,6,7,8]]
print('lst',lst)