string1='Machine Learning'
print(string1[::])
print(string1[1:4:1])
print(string1[::2])#it prints total string with step size 2
print(string1[2::])
print(string1[:2:])#it print from string1[0] to string[2] in step of 1
print(string1[-6::])#access from -6 to till the end of the string
print(string1[-1::-1])#retrieve from -1 to till first element from right to left


#repeating the string
s1='string1 '
print(s1*3)

#by slicing the string also we can repeat
print(s1[0:3]*3)


#concatenation of strings
s1='hello'
s2='python'
print(s1+s2)