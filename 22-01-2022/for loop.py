#For loop
#A python program to display characters of a string using for loop
str='srilekha'
for ch in str:
    print(ch)



#A python program to display each character from a string using sequence index
str='hello'
n=len(str)
for i in range(n):
    print(str[i])


#A python program to display odd numbers from 1 to 10 using range() object
for i in range(1,10,2):
    print(i)


#A program to display numbers from 10 to 0 in descending order
for x in range(10,0,-1):
    print(x)


#A program to display the elements of a list using for loop
list1=[1,2,3,4]
for element in list1:
    print(element)

#A python program to display and find the sum of a list of numbers using for loop
list2=[1,2,3,4,5,6]
sum=0
for i in list2:
    print(i)
    sum+=i
print('sum is:',sum)