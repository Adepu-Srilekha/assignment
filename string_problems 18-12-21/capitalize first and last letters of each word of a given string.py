#capitalize first and last letters of each word of a given string
string1='this  is  a  python  program'
print('string before:',string1)
def capital(string1):
    return ' '.join(map(lambda string1:string1[:-1]+string1[-1].upper(),string1.title().split()))
print('string after:',capital(string1))
