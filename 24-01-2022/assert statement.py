'''assert statement:
Is useful to check if a particular condition is fulfilled or not.
syntax:
assert expression,message
'''


#A python program to assert that user enters a number greater than zero
x=int(input('enter a number greater than 0:'))
assert x>0,'wrong input entered'#It checks here x>0 is true or not,if true then next statements will execute
#else it will display assertion error along with the 'message'
print('you entered:',x)


#A python program to handle the assertionerror exception that is given by assert statement.
x1=int(input('enter a number greater than 0:'))
try:
    assert (x1>0)
    print('you entered:',x1)
except AssertionError:
    print('wrong input entered:')