numb=int(input("enter any number:"))

facts=[]

for i in range(1,numb+1):

    if numb%i==0:

       facts.append(i)

print ("Factors of {} = {}".format(numb,facts))


















