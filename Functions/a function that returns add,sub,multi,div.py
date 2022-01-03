#A function that returns the results of addition,subtraction,multiplication,division
def add_sub_mul_div(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
'''w,x,y,z=add_sub_mul_div(8,4)
print('add',w)
print('sub',x)
print('mul',y)
print('div',z)'''

print('the results are:')
t=add_sub_mul_div(3,8)
for i in t:
    print(i)