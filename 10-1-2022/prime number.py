#prime number:
'''A prime number is a positive integer greater than 1
that has no other variables except 1 and the number itself. Since they have no other variables, the numbers 2, 3, 5, 7,
and so on are prime numbers.'''


'''number=int(input('enter a number:'))
#checking the number is greater than 1 or not
#since prime number starts from 2
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print('not prime',number)
            break
#need to give else statement under for loop because it is looping
    else:
            print('prime',number)
#if the number is less than 1
else:
    print('not a prime',number)'''


#print the prime numbers from 1 to 100

lower=int(input('enter the number:'))
upper=int(input('enter the number:'))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2, number):
            if (number % i) == 0:
                print('not prime', number)
                break
            # need to give else statement under for loop.....otherwise  it loops
        else:
            print('prime', number)








