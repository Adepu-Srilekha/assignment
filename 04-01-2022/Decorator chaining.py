'''Decorator chaining:we can define multiple decorators
for the same function'''

def decorfun(func):
    def inner():
        x=func()
        x+=1
        return x
    return inner
@decorfun
def outer():
    return 60
@decorfun
def outer1():
    return 100
print(outer())
print(outer1())




#multiplication


def decorfun1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decorfun(func):
    def inner():
        x=func()
        return 2*x
    return inner
@decorfun1
@decorfun
def outer():
    return 6
print('result is:',outer())