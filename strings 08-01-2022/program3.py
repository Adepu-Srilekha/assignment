#reverse a given string

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