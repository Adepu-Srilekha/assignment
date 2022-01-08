#Remove Duplicate characters from a string.
string1=input('enter a string:')
string2=[]
for x in string1:
    if x not in string2:
        string2.append(x)
str1=''.join(string2)
print(str1)