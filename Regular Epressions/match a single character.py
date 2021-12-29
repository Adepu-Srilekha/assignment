#match a single character
import re

randstr='12345'
#i want to print only 5th digit----5 it should print
print('matches:',len(re.findall('\d{5}',randstr)))