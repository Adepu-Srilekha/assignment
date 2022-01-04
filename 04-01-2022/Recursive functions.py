'''Recursive functions:
A function that calls itself is known as recursive functions.
eg:
factorial(3)=3*factorial(2)
            3*2*factorial(1)
            3*2*1*factorial(0)
            3*2*1*1
            6
formula:factorial(n)=n*factorial(n-1)

Advantages of Recursive functions:


reduce length of the code
improves readability
can solve complex problems easily'''
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print('factorial of 6 is:',factorial(6))

#using while loop
def fact(n):
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod
result=fact(5)
print('the factorial of 5 is:',result)