#write a python program
#input:a2
#output:aa
s=input("Enter Some String:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output = output + previous * (int(x) - 1)
print(output)