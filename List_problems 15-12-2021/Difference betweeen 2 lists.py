#Difference betweeen 2 lists
l1=[1,2,3,4,5]
l2=[2,3,7,5,8]
l1_as_set=set(l1)
l2_as_set=set(l2)
difference=l1_as_set.symmetric_difference(l2_as_set)
print('the difference is:',difference)
#converting to lists
difference_list=list(difference)
print('after converting to lists',difference_list)