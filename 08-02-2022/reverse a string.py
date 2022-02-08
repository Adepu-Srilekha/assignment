#Reverse a string
#1.using slicing
string1='srilekha'
string2=string1[::-1]
print(string2)


#2.using join and reversed function
str1='python'
str2=''.join(reversed(str1))
print('str2',str2)

#another method
input_str='technology'
input_list=list(input_str)
input_list.reverse()
reverse_string=''.join(input_list)
print('reverse string',reverse_string)