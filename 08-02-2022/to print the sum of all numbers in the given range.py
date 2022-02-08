#python program to print the sum if all numbers in the given range.
lower_range=12
upper_range=20
value=0
for i in range(lower_range,upper_range+1):
    value=value+i
print(value)

#another method using formula n+(n+1)/2
lower_range = 17
# given upper limit range
upper_range = 126
low_range = lower_range-1
# calculating the sum of natural numbers from 1 to lower limit range
lowSum = (low_range*(low_range+1))/2
# calculating the sum of natural numbers from 1 to upper limit range
highSum = (upper_range*(upper_range+1))/2
# calculating the sum of all numbers between the given range
rangeSum = highSum-lowSum
# printing the sum of all natural numbers between the given range
print("the sum of all numbers between",
      lower_range, "to", upper_range, "=", int(rangeSum))





