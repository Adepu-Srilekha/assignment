#Python program to check Leap year:having 366 days instead

given_year=int(input('enter a year'))
if given_year%4==0:
    if given_year%100==0:
        if given_year%400==0:
            print('given year',given_year,'is leap year')
        else:
            print('given year', given_year, 'is  not leap year')
    else:
        print('given year', given_year, 'is leap year')
else:
    print('given year', given_year, ' is not leap year')