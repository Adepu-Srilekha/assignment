#Python program to take in two strings and display the larger
#string without using built in functions.
first='python'
second='trending'
#initializing the lengths to 0
first_len=0
second_len=0

#using for loop to get the string length count

for char in first:
    first_len=first_len+1
for char in second:
    second_len=second_len+1
#comparing using if statements
if first_len>second_len:
    print(first,'is larger')
elif first_len==second_len:
    print('both are equal')
else:
    print(second,'is larger')

