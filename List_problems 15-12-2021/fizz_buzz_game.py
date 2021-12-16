num=int(input('enter how many numbers you want to enter:'))
def fizz_buzz(num):
    for num in range(1,num+1):
        if num %3 == 0 and num %5 == 0:
            print('fizzbuzz')
        elif num%3 == 0:
            print('fizz')
        elif num %5 == 0:
            print('buzz')
        else:
            print(num)
fizz_buzz(num)