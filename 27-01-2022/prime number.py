'''prime number:

a whole number greater than 1 that cannot be exactly divided by any
number other than itself and 1'''

num=int(input('enter a number:'))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,'not prime')
            break
    else:
        print(num,'prime number')
else:
    print(num,'not prime')
