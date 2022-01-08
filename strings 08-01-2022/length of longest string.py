string = str(input('enter a string:'))
string = string.split(' ')
ls1 = []
for i in string:
    ls1.append(len(i))
print('longest length of string: ', max(ls1))