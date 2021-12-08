#Dictionary Methods:
emp={'Nag':20,'vishnu':30}
emp.clear()#removes all key value pairs from dictionary
print(emp.clear())
print(emp)

#copy(copies all elements from emp to a new dictionary emp1
emp={'Nag':20,'vishnu':30}
emp1=emp.copy()
print(emp1)


#fromkeys()
#emp.fromkeys(s [,v])
#keys should be unique
#s is the sequence of keys and keys should be unique, and v is the value
#here we get same value to the keys in sequence
emp = emp.fromkeys([1,2,2,4],2.9)
print(emp)
#print(emp.fromkeys('Nag'[30])

#to print all unique values in the dictionary
emp1=emp1.fromkeys(['srilekha','shital','rakshitha'],100)
print(emp1)

print(emp.items())
print(emp.keys())
print(emp.values())
#update()
#