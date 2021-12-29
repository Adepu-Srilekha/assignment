import re
str='sat,hat,mat,pat,qwe,bat'
#what is the pattern here... at is common in all
allstr=re.findall('[shmpb]at',str)
#words starting with shmp and ending with at
for i in allstr:
    print(i)
