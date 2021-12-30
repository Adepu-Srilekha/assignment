import re
str='one two three'
#\A is useful to match the words at the begining of a string
#\Z is useful to match the words at the end of the string
result=re.findall(r't[\w]*\Z',str)
print(result)