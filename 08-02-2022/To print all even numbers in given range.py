#To print all even numbers in given range
lower=int(input('enter a number:'))
upper=int(input('enter a number:'))
for number in range(lower,upper+1):
    if number%2==0:
        print(number)

