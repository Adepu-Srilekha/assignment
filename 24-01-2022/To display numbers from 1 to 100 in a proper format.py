#A python program to display numbers from 1 to 100 in a proper format.
#displaying numbers from 1 to 100 in 10 rows and 10 columns.
for i in range(1,11):
    for j in range(1,11):
        print('{:8}'.format(i*j),end='')
    print()