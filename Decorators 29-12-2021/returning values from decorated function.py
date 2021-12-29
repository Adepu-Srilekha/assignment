#returning the value from decorated function

def func1(function):
    def wrapper(*args,**kwargs):
        print('worked')
    return wrapper
@func1  
def func2(name):
    print(f'{name}')

func2('python')


