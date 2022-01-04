#division using decorators
def division1(func):
    def inner(a,b):
        print('we are dividing', a ,'with', b)
        if b==0:
            print('we cannot divide')
        else:
            return func(a,b)
    return inner
@division1
def division(a,b):
    return a/b
print(division(100,0))
