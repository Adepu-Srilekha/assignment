#Remove duplicates from a list of lists

#creating a list of lists
list1=[[1,2,3],[7,8,9],[2,1,7],[7,8,9],[1,5,3],[1,2,3]]
dup_free=[]
for i in list1:
    if i not in dup_free:
        dup_free.append(i)
print(dup_free)
