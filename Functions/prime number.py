#prime number:Divisible by only 1 and itself(2,3,5,7)
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input('enter a number:'))
result=prime(num)
if result==1:
    print('prime')
else:
    print('not prime')
