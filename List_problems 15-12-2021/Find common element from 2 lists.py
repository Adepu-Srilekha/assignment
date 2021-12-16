#Find common element from 2 lists
list1=[1,2,3,4,5,6]
list2=[2,7,6,4,1,9]
list_as_Set1=set(list1)
list_as_set2=set(list2)
common_elements=list_as_Set1.intersection(list_as_set2)
print('the common elements are',common_elements)
#again converting to list
common_list=list(common_elements)
print('common_list',common_list)