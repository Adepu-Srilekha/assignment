#continue statement
#when continue is executed, the subsequent statements in the loop are not executed.
x=0
while x<=15:
    x+=1
    if x>2:#if x>2 then continue next iteration
        continue
    print('x=',x)
print('out of loop')
#A python program to display numbers from 1 to 5 using continue statement.
x=0
while x<=15:
    x+=1
    if x>5:#if x>5 then continue next iteration
        continue
    print('x=',x)
print('out of loop')