#without decorator symbol
def decorfunc(func):
    def inner():
        value=func()
        value+=2
        return value
    return inner
def outer():
    return 34
result=decorfunc(outer) #take the function name and pass the arguement as outer function and assign to a variable.
print(result())


#with decorator


def decorfunc(func):
    def inner():
        value=func()
        value+=2
        return value
    return inner
@decorfunc
def outer():
    return 34
print('with decorator:',outer())

#If we give return statement in the function... then while calling we need to give print statement.
#If we give print statement in the function... directly call the function.


#using print

def decorfunc(func):
    def inner():
        value=func()
        value+=2
        print(value) #using print
    return inner
@decorfunc
def outer():
    return 70
outer() #directly calling the function