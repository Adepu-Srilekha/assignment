#generate an iterator
#Basically we print the starting and ending index of the matching object
import re
str='we need to inform him with the latest information'
for i in re.finditer('inform',str):
    #converting to tuple
    loctup=i.span()
    print(loctup)
