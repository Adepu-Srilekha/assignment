#remove spaces from a string:
string1='python is very trending   technology      '
'''string2=string1.replace('   ','')
print(string2)'''

#using join
string3 = " ".join(string1.split())
print(string3)


#using rstrip()
#Python rstrip() function is used to remove the spaces at the right side of a string.
string4=string1.rstrip()
print('string4',string4)

#using lstrip()
string5=string1.lstrip()
print('string5',string5)

#using strip()
#Python strip() function is used to remove the spaces at both sides of a string
my_string1='    helllo how r u  '
string6=my_string1.strip()
print(string6)