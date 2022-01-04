def decorfun(func):
    def inner():
        x=func()
        x+=2
        return x
    return inner
@decorfun
def outer():
    return 15
res=outer()
print(res)



def decorfun(func):
    def inner():
        x=func()
        x+=2
        return x
    return inner
@decorfun
def outer():
    return 45
print('the result is:',outer())
#If we are using return statement... need to write print statement.