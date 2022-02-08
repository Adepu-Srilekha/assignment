#Handling precision values

#1.using % operator --syntax:'%.point'%number


input1=123456.98867
#The no.of decimal points after the dot will be eliminated
res='%.2f'%input1
print('The result is:',res)


#2.using format function--syntax:'{0:pointf}'.format(number)
res2='{0:.3f}'.format(input1)
print('res2',res2)

#3.using round() function----syntax:round(number,point)

res3=round(input1,4)
print('res3',res3)



