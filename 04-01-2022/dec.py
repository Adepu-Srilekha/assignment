def decoratorfunc(func):
    def inner():
        x = func()
        x = x + 1
        return x
    return inner

def outer():
    return 10

temp = decoratorfunc(outer)
var = temp()
print(var)


def decoratorfunc(func):
    def inner():
        x = func()
        x = x + 1
        print(x)
    return inner

@decoratorfunc
def outer():
    return 10

@decoratorfunc
def outer1():
    return 20

outer()
outer1()



def decorfunc(function):
    def inner():
        value=function()
        value+=2
        print(value)
    return inner
@decorfunc
def outer3():
    return 10
outer3()