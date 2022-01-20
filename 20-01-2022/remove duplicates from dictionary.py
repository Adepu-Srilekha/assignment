#Remove duplicates from Dictionary:
dict1=[{'a':20},{'b':70},{'c':90},{'b':70},{'c':90}]
print(dict1)
dict2=[]
for i in range(len(dict1)):
    if dict1[i] not in dict1[i+1:]:
        #print('dict1[i+1]',dict1[i+1])
        dict2.append(dict1[i])
print(dict2)
