import re
str='Lekha got 45 marks,Sri got 55 marks'

#extracting only marks having 2 digits
marks=re.findall('\d{2}',str)
print(marks)

#extracting names starting with Capital letter,and remaining alphabetic charaters
names=re.findall('[A-Z][a-z]*',str)
print(names)
