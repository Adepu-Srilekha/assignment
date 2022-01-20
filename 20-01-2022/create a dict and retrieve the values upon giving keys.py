dict1={}
n=int(input('enter how many elements'))
for i in range(1,n+1):
    keys=input('enter the keys:')
    values=input('enter the value:')
    dict1[keys]=values
print(dict1)

#to get the value by giving the keys
print('salary is',dict1['salary'])