import re
str='srilekha:123456789'
result=re.search(r'\D+',str)
print(result.group())
#\D represents all characters except numeric characters.
#\D+... gives total string
#+ represents 1 or more repititions
#* represents 0 or more repitions
