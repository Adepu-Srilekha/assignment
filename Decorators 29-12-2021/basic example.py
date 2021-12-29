def function1(function):
    #inside the decorator we are using arguements 
    def wrapper (*args,**kwargs):
        print('hello')
        function(*args,**kwargs)
        print('welcome')
    return wrapper
@function1
def function2(name):
    print (f'{name}')

function2('srilekha')

#used arguements in the decorator




