input_string1 = input("Enter string:")
output = ''
for i in range(len(input_string1)):
    if input_string1[i] == '.':
        output = output + ','
    elif input_string1[i] == ',':
        output = output + '.'
    else:
        output = output + input_string1[i]
print(output)