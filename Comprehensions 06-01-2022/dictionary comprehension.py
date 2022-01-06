#Dictionary comprehension
#manipulating existing dictionary and creating a new dictionary
diction1={'srilekha':20,'shital':30,'rakshitha':30}
for i in diction1.items():
    print('diction1',i)
#syntax :
#{k:v for k,v in dictioary_name.items()}
print('Dictionary comprehension1')
dict_comp1={k:v for k,v in diction1.items()}
print(dict_comp1)



dict_comp1={k:v**2 for k,v in diction1.items()}
print(dict_comp1)
list_tup=[(1,'a'),(2,'b'),(3,'c')]




print('creating dictionary by using for loop')
dict1={}
for element in list_tup:
    dict1[element[0]]=element[1]
print('Dict comp2 by using lists')
dict_comp={element[0]:element[1] for element in list_tup}
print(' dict compos',dict_comp)

print('using generator function dict comprehension')
dict3=dict(element for element in list_tup)
print(dict3)

dict5={i:i**2 for i in range(4)}
print(dict5)

print('converting to strings')
dict5={i:str(i) for i in range(4)}
print(dict5)

print('using sequences')
dict6={i:i**2 for i in [1,2,3,4,5,6]}
print(dict6)

print('using if statement in dictionary')
ages={'jack':30,'john':20,'michael':35,'guido':50}
ages_comp={k:v for k,v in ages.items() if v>=35}
print('using if',ages_comp)



print('using if else statements')
ages_comp1={(k if k=='jack' else 'jill'):v for k,v in ages.items()}
print('if else',ages_comp1)# takes the last value for the jill


age1={'jack':30,'jill':39,'michael':50}
ages_comp2={k:('old' if v>40 else 'young') for k,v in age1.items()}
print('ages comp2',ages_comp2)

#we can have if else conditions with keys  and values and both
#and we can also have if else with for loop


