#A python program to find the first occurence of an element in a tuple.
str=input('Enter elements seperated by commas:').split(',')
lst=[int(num) for num in str]
tup=tuple(lst)
print('The tuple is:',tup)
ele=int(input('Enter an element to search:'))
try:
    pos=tup.index(ele)
    print('Element position no:',pos)
except:
    print('Element not found in tuple')