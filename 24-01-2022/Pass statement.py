'''Pass statement:
Pass statement does not do anything..
Used with 'if ' statement or inside forloop to represent no operation.
'''

#A program to know that pass does nothing
x=0
while x<10:
    x+=1
    if x>5:
        pass
    print('x',x)
print('out of loop')