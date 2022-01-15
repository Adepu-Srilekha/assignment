l=[1,2,3,4,5]
square=list(map(lambda x:x*x,l))
print(square) #[1, 4, 9, 16, 25]


l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)