#palindrome
def palindrome(s):
    if s.lower()==s[::-1].lower():
        print('yes')
    else:
        print('No')
string1=input('enter a string:')
res=palindrome(string1)
print(res)