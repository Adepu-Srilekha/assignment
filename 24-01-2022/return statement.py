#return statement:
#This function represents a group of statements to perform a task

#To write a function that returns the result of sum of two numbers.
def sum(a,b):
    return a+b
#calling the function
res=sum(3,2)
print('the result is:',res)

#Write a program to display prime number series
input1=int(input('upto what number:'))
for num in range(2,input1+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)