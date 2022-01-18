def reverse_string(mystring):
    mylist=list(mystring)
    mylist.reverse()
    mystring=''.join(mylist)
    return mystring
mystring='hello python'
res=reverse_string(mystring)
print(res)

#for one string:
def reverse(str1):
    str=''
    for i in str1:
        str=i+str
    return str
res1=reverse(str1='srilekha')
print(res1)