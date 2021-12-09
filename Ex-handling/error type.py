'''a=2
if a>3
print(a)'''

#this is the syntax error
#zero division error type it is

dir(__builtins__)
#it gives builtin error types that python handles.

'''compile time errors:
1.syntax errors (if a>1.......colon at the end)
2.indentation errors(spaces and tab if not given properly)

print('...........Run time errors...........')
def concat(a,b):
    print(a+b)

concat(25,'lekha')'''''''''
print('....using exceptions.......')
def concat(a,b):
    try:
        a=10
        b='python'
        print(a+b)
    except Exception as e:
        print('the error is',e)

concat(10,'python')
#The run time errors which can be handled by the programmer are called exceptions.
