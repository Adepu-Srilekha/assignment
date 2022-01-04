#calling the function without using decorators
def decor(func):
    def inner(name):
        if name=='srilekha':
            print('Hello srilekha bad morning')
        else:
            func(name)
    return inner
def wish(name):
    print('hello',name,'good morning')

result=decor(wish) #calling the function...pass the arguement also a function
result('Rakshitha') #here we need to pass the names with the assigned variable
result('Shital')
result('srilekha')
