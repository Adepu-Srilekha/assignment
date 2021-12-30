import re
str='one two three four five six seven 8 9 10'
#\b represents a space
result=re.findall(r'\b\w{3,5}\b',str)
print(result)


#To retrieve single digit
result=re.findall(r'\b\d\b',str)
print(result)
