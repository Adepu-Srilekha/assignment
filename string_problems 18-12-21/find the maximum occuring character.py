string1='this is a python program'
frequency={}
for x in string1:
    if x in frequency:
        frequency[x]+=1
    else:
        frequency[x]=1
result=max(frequency,key=frequency.get)
print('the maximum of all',str(result))
print(frequency)
