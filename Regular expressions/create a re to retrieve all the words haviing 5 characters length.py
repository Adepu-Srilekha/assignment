import re
str='an apple a day keeps the doctor away'
#\b represents a space
#\w{5} represents a word containing any alphanumeric characters repeated for 5 times
result=re.findall(r'\b\w{5}\b',str)
print(result)

#using search
result=re.search(r'\b\w{5}\b',str)
print('using search',result.group())
#to retrieve the word use group
