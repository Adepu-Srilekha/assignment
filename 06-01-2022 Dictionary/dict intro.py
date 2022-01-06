'''If we want to represent a group of objects as key-value
pairs then we should go for dictionary
eg:
rollno:12
phone_number:122445


Features of dictionary:

Duplicate keys are not allowed,but values are allowed

heterogeneous objects are allowed for both key and values(means all data types)

insertion order is not preserved

dictionaries are mutable

dictionaries are dynamic

indexing and slicing concepts are not applicable'''

#creating an empty dictionary:
d={}
d=dict()

d[1]='srilekha'
d[2]='lekha'
print(d)

#Accessing the data from dictionary:
print('accessing',d[1])





dictionary1={}
n=int(input('enter no.of students:'))
for i in range(1,n+1):
    name=input('Enter Student Name:')
    percent=int(input('enter percentage of marks:'))
    dictionary1[name]=percent
print(dictionary1)
print('Name of the student\t\t\t %of marks')
for i in dictionary1:
    print('\t',i,'\t\t\t\t\t\t',dictionary1[i])


#updating Dictionary:
dict2={'a':1,'b':2}
dict2['c']=3
print(dict2)

#how to delete elements from dictionary
dict2={'a':1,'b':2}
del dict2['a']
print(dict2)



























