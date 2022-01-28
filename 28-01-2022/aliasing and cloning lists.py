x=[1,2,3,4,5]
y=x
print(y)
print(x)
#x is cloned as z
z=x[:]
print('z',z)
x[1]=44
print('after modifying',x)
print(y)
print(z)


s=x.copy()
print('s',s)