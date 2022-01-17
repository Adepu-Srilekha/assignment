string1='hello python'
n=len(string1)
i=0
while i<n:
    print(string1[i],end=' ')
    i+=1
print()#to print next line
i=-1
while i>=-n:
    print(string1[i],end=' ')
    i-=1

#using for loop
print('.........using for loop.......')
string2='hello world'
for i in string2:
    print(i,end=' ')

print()
#to access in reverse order
for i in string2[::-1]:
    print(i,end=' ')



