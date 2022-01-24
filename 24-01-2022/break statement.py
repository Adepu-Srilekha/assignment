#It is used inside the while loop or forloop to come out of the loop.
x=10
while x>=1:
    print('x=   ',x)
    x-=1
print('out of loop')

#A python program to display numbers from 10 to 6 and break the loop
x=10
while x>=1:
    print('x=',x)
    x-=1
    if x==5:
        break
print('out of loop')