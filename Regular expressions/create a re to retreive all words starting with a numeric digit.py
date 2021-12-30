import re
str='The meeting will be conducted on 1st and 2nd of every month'
result=re.findall(r'\d[\w]*',str)
for word in result:
    print(word)