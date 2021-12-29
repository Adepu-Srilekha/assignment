#replace a particular string
import re
food='hat rat mat pat'
#to replace rat with food
regex=re.compile('[r]at')
food=regex.sub('food',food)
print(food)