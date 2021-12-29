#Decorators provides additional functionality for class or method
def summ(a,b):
    result=a+b
    return result
print(summ(2,9))#one time usage & direct function call
print('The sum is:',summ(2,3))

#2 places or more places
output=summ(2,9)
print(output) #first usage
print(output+100)#second usage

