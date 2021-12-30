import re
str='Lekha 1 2-10-1997,Sita 2 21-22-1999 Rani 3 1-1-2000'
result=re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(result)

