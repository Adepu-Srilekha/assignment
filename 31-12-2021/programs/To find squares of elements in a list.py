def squares(x):
    return x*x
list1=[1,2,3,3,4]
list2=list(map(squares,list1))
print(list2)