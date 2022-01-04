#A python program to create two decorators.
def decoratorfunc(func):
    def inner():
        x=func()
        x+=1
        return x
    return inner
@decoratorfunc
def outer():
    return 45
@decoratorfunc
def outer1():
    return 90
print(outer())
print(outer1())

