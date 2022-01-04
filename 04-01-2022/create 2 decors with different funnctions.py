def decfunc1(func):
    def inner():
        x=func()
        x+=6
        return x
    return inner

def decfunc2(func):
    def inner():
        x=func()
        x*=2
        return x
    return inner
@decfunc1
@decfunc2
def outer():
    return 45
print(outer())