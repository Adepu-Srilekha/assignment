#To retrieve only the first letter from group of words
words=['apple','banana','grapes','orange']
lst=[]
for i in words:
    lst.append(i[0])
print(lst)
#through list comprehension
lst1=[w[0] for w in words]
print(lst1)


#Lets take two lists num1 and num2 and create a new list num3 with numbers present in num1 but not in num2
num1=[1,2,3,4,5]
num2=[10,11,1,2]
set1=set(num1)
set2=set(num2)
set3=set1.difference(set2)
print(set3)
list1=list(set3)
print('list1',list1)


#without converting to sets.
num1=[1,2,3,4,5]
num2=[10,11,1,2]
num3=[]
for i in num1:
    if i not in num2:
        num3.append(i)
print('num3',num3)


#creating a dictionary comprehension
dict1={i:i+2 for i in range(1,5)}
print('dict1',dict1)



