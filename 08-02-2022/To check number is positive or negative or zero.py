#python program to check if a number is positive negative or zero
def check(given_number):
    if given_number>0:
        print('positive')
    elif given_number<0:
        print('negative')
    else:
        print('zero')
given_number=int(input('enter a number:'))
print(check(given_number))

