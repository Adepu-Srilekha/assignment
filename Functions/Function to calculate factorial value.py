#Factorial of a number:
#eg:4!=4x3x2x1
def fact(n):
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod
'''fact(4)
print(fact(4))'''
for i in range(1,6):
    print('the factorial of {} is {}'.format(i,fact(i)))