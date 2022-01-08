#we use find(),rfind(),index(),rindex()
#rfind and rindex methods search for substring from right to left
#methods to find substring
#syntax :
#string1.find(substring,begining,end)
#it gives the the position of substring in string1
string1=input('enter a string1:')
sub=input('enter substring:')
n=string1.find(sub,0,len(string1))
print(n)