def finding_largest(num1,num2,num3):
    if (num1>=num2) and (num1>=num3):
        return num1
    #comparing num2 with other two nums
    elif(num2>=num1) and (num2>=num3):
        return num2
    else:
        return num3
num1=12
num2=8
num3=7
res=finding_largest(num1,num2,num3)
print(res)

#using in-built function
number1 = 3
number2 = 5
number3 = 7
# using max function to find largest numbers
maxnum = max(number1, number2, number3)
print("The largest number among the three numbers =",
      maxnum)
