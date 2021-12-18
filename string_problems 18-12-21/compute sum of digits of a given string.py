string1='12345678'
sum_digit=0
for x in string1:
    if x.isdigit():
        sum_digit+=int(x)
print('sum of digits',sum_digit)