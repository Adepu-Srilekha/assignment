nums=[7,6,5,4,9,8,3,2,1]
num1=list(filter(lambda x:x%2==0,nums))#even
print(num1)

num2=list(filter(lambda x:x%2!=0,nums))#odd
print(num2)
