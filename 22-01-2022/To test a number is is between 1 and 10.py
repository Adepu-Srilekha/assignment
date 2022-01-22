#A python program to test whether a given number is in between 1 and 10.
input1=int(input('enter a number:'))
if input1>=1 and input1<=10:
    print('you typed ',input1,'which is between 1 and 10')
else:
    print('you typed',input1,'which is below 1 or above 10')