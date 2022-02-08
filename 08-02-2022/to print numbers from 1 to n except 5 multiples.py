#python program to print numbers from 1 to n except 5 multiples
numb=20
for i in range(1,numb+1):
    if (i%5!=0):
        print(i)