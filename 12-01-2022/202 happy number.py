#324=3^2+2^2+4^2=29 is
#Happy number
num=int(input('enter a positive number:'))
sum=0
while num!=0:
    #it will loop and starts from the last number to first number
    rem=num%10
    sqr=rem*rem
    #will get last numbers square and store it in sum
    sum=sum+sqr
    num=int(num/10)

print(sum)
'''if num.isnumeric():
    num=num.replace(num,sum)
print(num)'''