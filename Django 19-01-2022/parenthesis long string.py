string = input("Enter string: ")

close = 0
open = 0

for char in string:
    if char == '(':
        close += 1
    else:
        open += 1

if close < open:
    length = close * 2
else:
    length = open * 2

print("Length of longest substring is: ",length)

