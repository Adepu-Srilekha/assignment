#compute sum of digits of a given string.
string1=input('enter a string:')
sum_digit=0
for x in string1:
    if x.isdigit():
        sum_digit+=int(x)
print(sum_digit)