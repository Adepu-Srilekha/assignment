'''Function Decorators:
Is a function which takes function as arguement
 extend its functionality and
 returns modified function with extended functionality.

 The main objective of decorator:
 Extend the functionality of existing functions without
 modifying that function'''

def wish(name):
    print('hello',name,'good morning')
wish('lekha')
#this function always print same output for any name

#we can modify this function to provide different messages using decorators.
def decor(func):
    def inner(name):
        if name=='srilekha':
            print('Hello srilekha bad morning')
        else:
            func(name)
    return inner
@decor
def wish(name):
    print('hello',name,'good morning')

wish('srilekha')

'''advantage: comment the feature when we want,dry software:do not repeat
disadvantages
purpose of decorator
types of decorators
wrapper function
pyton decorators
django decorators

what is the decorator execution if multiple decorator exists'''
