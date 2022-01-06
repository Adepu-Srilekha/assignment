'''get():
Get the value associated with the key'''
dict2={'a':1,'b':2}
print('using get',dict2.get('a'))

print('using default value',dict2.get('c','sss'))
#if the key is not present in the dictionary it gives the default value.

'''1.pop():
It removes the entry associated with the specified key '''

print(dict2.pop('a'))
print(dict2)

'''2.popitem():It removes the last item from the dictionary'''


dict2={'a':1,'b':2}
print('popitem',dict2.popitem())
print(dict2)

#clear:removes all the elements from the dictionary
dict2={'a':1,'b':2}
print('using clear',dict2.clear())
print(dict2)



#keys():returns all the keys associated with dictionary
dict3={'a':1,'b':2}
print('keys',dict3.keys())


#values(): returns all the values associated with the dictionary
dict3={'a':1,'b':2}
print('values',dict3.values())


#we can also print values and keys like this using for loop
for keys in dict3.keys():
    print(keys)

for values in dict3.values():
    print(values)


#items():returns items or list of tuples representing key-value pairs
for k,v in dict3.items():
    print('items',k,':',v)
dict2 = {'a': 1, 'b': 2}
dict4=dict2.copy()
print('dict4',dict4)

#setdefault():
#If key is already availble then this function returns that value
#If key is not available then the specified key-value will be added.
dict5={'a':1,'b':2,'c':5}
print('setdefault',dict5.setdefault('d',2))#d and 2 will be added because it is not present in the dict
print(dict5)
print('setdefault1',dict5.setdefault('c',5))
print('....',dict5)



#update()
#d1.update(d):all items present in the dict 'd' will be added to d1.
diction3={'name':'srilekha','company':'MCS'}
dict6={}
dict6.update(diction3)
print('dict6',dict6)

#1.write a program to take dictionary from the keyboard and print sum of the values.
print('Enter a dictionary')
diction4={}
no_items=int(input('Enter how many items:'))
for i in range(1,no_items+1):
    name=input('enter name:')
    marks=int(input('enter the marks:'))
    diction4[name]=marks
print(diction4)
print('sum of values:',sum(diction4.values()))


#2.write a program to find number of occurences of each letter present in the
#given string.

string1=input('Enter a string:')
d={}
for x in string1:
    count = string1.count(x)
    d[x] = count
print(d)
for k,v in d.items():
    print(k,'occured',v,'times')













#copy():To create exactly duplicate dictionary(cloned copy)

