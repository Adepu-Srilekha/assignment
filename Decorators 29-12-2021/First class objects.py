def func1(name):
    return f'Hello {name}'

def func2(name):
    return f'How are you {name}'

def func3(func4):
    return func4 ('Dear Learner')

print(func3(func1))
print(func3(func2))


#here we can also pass functions as arguements.that is how we use the first class objects.
