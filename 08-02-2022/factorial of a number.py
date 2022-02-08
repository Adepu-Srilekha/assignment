#Factorial of  a number

def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=5
res=fact(num)
print(res)
