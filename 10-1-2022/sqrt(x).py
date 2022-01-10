'''def square(x):
    return x**x
x=4
a=square(x)
print(a)'''

'''number = 10
square_root = number**(1/2)
print(square_root)
a=round(square_root,2)
print(a)'''

def floorSqrt(x):
    # Base cases
    if (x == 0 or x == 1):
        return x

    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i

    return i - 1


# Driver Code
x = 16
print(floorSqrt(x))