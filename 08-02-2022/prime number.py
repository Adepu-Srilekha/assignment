#print the prime number between 100 to 200
lower=int(input('enter starting number'))
upper=int(input('enter ending number:'))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                print('not prime',number)
                break
        else:
            print('prime',number)