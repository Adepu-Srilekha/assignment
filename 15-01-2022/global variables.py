'''The variables which are declared outside of function are called global variables.
These variables can be accessed in all functions of that module'''
a=10
def func1():
    print(a)

def func2():
    print(a)

func1()
func2()
