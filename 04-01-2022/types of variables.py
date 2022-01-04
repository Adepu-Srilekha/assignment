''''#Types of variables:
#python supports 2 types of variables
#1.Global
#2.Local
Global variables---declared outside of function
                ---can be accessed in all functions of that module'''
a=10
def func1():
    print(a)
def func2():
    print(a)
func1()
func2()


'''2.Local variables:----inside a function
                    ----- only available for the function
                    ---- outside cannot access'''
def function1():
    a=2
    print(a)
function1()


#Below statement is not valid for Local variables.
def function2():
    print(a) #invalid
function2()





def f1():
    a=10
    print(a)
def f2():
    print(a)
f1()
f2()