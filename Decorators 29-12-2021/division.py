'''def div(a,b):
    if a<b:
        a,b=b,a

    print(a/b)

div(3,9)
'''
#here the numerator should be higher than the dinominator
#so swapping


#suppose you want to swap those values without touching the code
#thats where decorators comes into picture


#using decorators we can add extra features in the function

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)





