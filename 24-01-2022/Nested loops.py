#we can write a for loop inside a while loop or a for loop inside another for loop..such loops
#are called while loops.

#inside for loop is looping in range 3 and 4 times
for i in range(4):
    for j in range(3):
        print('i=',i,'\t','j=',j)

#the output is for i=0,j will run in range3..i=0 j=0 ,i=0 j=1,i=0 j=2,i=0 j=3


#another example
for k in range(2):
    for l in range(3):
        print('k=',k,'\t','l=',l)


#k=0 l=0 ,k=0 l=1,k=0 l=2

#another example
for i in range(1,11):
    for j in range(1,i+1):
        print('star example','i=',i,'\t','j=',j )


#to print star
for i in range(1,11):
    for j in range(1,i+1):
        print('*',end='')
    print()
#i.....no.of rows






