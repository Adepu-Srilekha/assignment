#reverse a  string:
string1=input('enter a string:')
reversed_string=string1[::-1]
print(reversed_string)


#using built-in function
string2=input('enter a string:')
result=''.join(reversed(string2))
print(result)

#using for loop

def rever_string(s):
    t=''
    for i in s:
        t=i+t#appending chars in reverse order
    return t
input1=input('enter the string:')
res=rever_string(input1)
print(res)