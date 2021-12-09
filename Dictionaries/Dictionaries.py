dict1={'name':'chandra','id':234,'salary':9090}
print(dict1)
print(dict1['name'])#returns the value
#accessing the value
print('the name of the employee is',dict1['name'])
#to access the elements we cannot give like dict1[0] but instead we should mention the keyname inside bracket
#to check how many key value pairs
print(len(dict1))
#key and value pair treats as one element
#we can modify the value in the dictionary like
dict1['salary']=10000
print(dict1)
print(dict1['salary'])
#we can also insert new key-value pair into the existing dictionary and adds at the end of the dict
dict1['branch']='CNIS'
print(dict1)
#to delete the key-value pair from the dictionary
del dict1['id']
print(dict1)
#to check whether a key is available in the dict we use... in and not in.. it returns true or false
print('......checking in and not in......')
print('branch' in dict1)


#The value can be a number,list,strings,tuple or another dictionary.
#the keys should be immutable type.. we  can use a number,string,tuples as keys since they are immutable.
#we cannot use dictionaries and lists as keys
#eg:
emp={['Nag']:20,'vishnu':30,'Nag':10}
print('details',emp)
#we get error as unhashable type

#But keys should follow the rules
'''1.keys should be unique.. no duplicate keys
2.If we enter the same key again, the old key will be over written and new key will be available'''
#eg:
emp={'Nag':20,'vishnu':30,'Nag':10}
print(emp)
#here new key is replaced,and old key such as nag:20 will be overwritten with the new key.


