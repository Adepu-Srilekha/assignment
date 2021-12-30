import re
str='an apple a day keeps the doctor away'
result=re.findall(r'a[\w]*',str)
for word in result:
    print(word)