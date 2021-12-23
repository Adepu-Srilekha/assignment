# Remove odd index values
str = input("enter your string:")
res = ""
for i in range(len(str)):
#    print(i)
    if i%2!=0:
        res = res+str[i]
print(res)

