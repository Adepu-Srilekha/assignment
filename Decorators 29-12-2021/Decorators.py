'''Decorators is the design pattern of python that allows the
user to add functionality to an existing object without
modifying its structure'''
#Decorators usually called before the definition of the function
#you want to decorate.

def func1 (function1):
    #This is the inner function basically the decorator we are going to use
    def wrapper():
        print('hello')
        function1()
        print('welcome')
    return wrapper
@func1 #syntactic sugar ..makes the job easier
def func2():
    print('python')

func2()



