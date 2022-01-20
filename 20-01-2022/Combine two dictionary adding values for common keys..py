#Combine two dictionary adding values for common keys.
dict1={'a':1,'b':2,'c':3}
dict2={'c':3,'d':4,'e':2}
for key in dict2:
    if key in dict1:
        dict2[key]=dict2[key]+dict1[key]
    else:
        pass
print(dict2)