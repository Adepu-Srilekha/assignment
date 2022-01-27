#second largest number:
mylist=[1,2,3,4,5,6]
print('original list',mylist)
new_list=set(mylist)
new_list.remove(max(new_list))
print('The second largest number:',max(new_list))



#another method
mylist=[80,90,30,20]
largest=mylist[0]
second_largest=mylist[0]
for i in range(1,len(mylist)):
    if mylist[i]>largest:
        second_largest=largest
        largest=mylist[i]
    elif mylist[i]>second_largest:
        second_largest=mylist[i]
print('The second largest number is',second_largest)
