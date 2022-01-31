#A python program to accept elements in the form of a tuple and display their sum and average.

num=eval(input('Enter elements in ():'))
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print('sum of numbers:',sum)
print('Average of numbers:',sum/n)
