dict1={}
n=int(input('enter number of elements:'))
for i in range(1,n+1):
    keys=input('enter keys:')
    value=int(input('enter values:'))
    dict1[keys]=value
print(dict1)
res=sum(dict1.values())
print(res)