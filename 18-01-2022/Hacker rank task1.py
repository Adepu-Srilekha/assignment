'''Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6  to 20 , print Weird
If n is even and greater than 20 , print Not Weird
Input Format

A single line containing a positive integer, n.'''
'''n=int(input('enter any number:'))
def check_even(n):
    for i in range(n):
        if i%2==0:
            if 6<=i>=20:
                print(i,'weird')
            elif 2<=i<=5 or i>20:
                print(i,'not weird')
        else:
            print(i,'weird')
check_even(n)'''

'''list1=[]
n=int(input('enter a number'))
for i in range(n):
    print(i)
    list1.append(i)
print(list1)
lst2 = []
for x in list1:
    x = str(x)
    lst2.append(x)
print('lst',lst2)
string = ''.join(lst2)
print(string)
'''

n=int(input('enter any number:'))
def check_even(n):
    if n%2==0:
        if 6<=n>=20:
            print(n,'weird')
        elif 2<=n<=5 or n>20:
            print(n,'not weird')
    else:
        print(n,'weird')
result=check_even(n)
print(result)




