string1=input('enter a string1')
string2=input('enter a string2')
flag = False
if len(string1)==len(string2):
    for char in string1:
        if char in string2:
            flag=True
        else:
            flag=False
            break
if flag == True:
    print('Anagram')
else:
    print('Not an anagram')