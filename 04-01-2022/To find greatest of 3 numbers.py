def greatest(x,y,z):
    if (x>y)and (x>z):
        largest=x
    elif (y>x) and (y>z):
        largest=y
    else:
        largest=z
    return largest

print(greatest(1,8,9))