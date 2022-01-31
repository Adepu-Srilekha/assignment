#A python program to find common elements in two lists.
#Taking two lists
list1=['srilekha','shital','rakshitha','lekha']
list2=['srilekha','Vinay','rakshitha','govind']


#converting them to sets
set1=set(list1)
set2=set(list2)

set3=set1.intersection(set2)
print(set3)


#converting the resultant set to list
set4=list(set3)
print(set4)