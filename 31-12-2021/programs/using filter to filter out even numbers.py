def is_even(x):
    if x%2==0:
        return True
    else:
        return False
list1=[1,2,3,4,5]
list2=list(filter(is_even,list1))
print(list2)