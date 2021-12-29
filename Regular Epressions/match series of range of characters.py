#Match series of range of characters
import re
str='Sat,hat,mat,pat'
someStr=re.findall('[h-z]at',str)
for i in someStr:
    print(i)
    #here s is not printed because it starts with capital

#^[h-z]----means everything apart from h to z