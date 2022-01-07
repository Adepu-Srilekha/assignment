#Find the list in a list of lists whose sum of elements is the highest

list1=[[1,2,3,5,6],[4,5,6,8],[3,7,8,9]]
list2={}
for i in list1:
    list2[sum(i)] = i
print(list2)
maxval = 0
for key in list2.keys():
    if maxval < key:
        maxval = key
print(maxval)
print(list2.get(maxval))



