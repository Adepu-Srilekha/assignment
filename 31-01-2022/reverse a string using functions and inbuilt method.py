string1=input('enter a string:')
reversed1=''.join(reversed(string1))
print(reversed1)

#reverse a string using functions
def reverse(s):
    i=''
    for j in s:
        i=j+i
    return i
st='lekha'
res=reverse(st)
print(res)