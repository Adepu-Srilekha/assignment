#Reverse a given string  Input : "Python"   Output : "nohtyP"
string1='Python'
i=0
for i in string1:
    print(i,end='')
print()

for i in string1[::-1]:
    print(i,end='')
print()


#using while loop
print('using while loop')
string2='Learning'
n=len(string2)
i=0
while i<n:
    print(string2[i],end='')
    i+=1
print()
i=-1
while i>-n:
    print(string2[i],end='')
    i-=1



