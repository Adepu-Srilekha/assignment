#Check list is empty or not using functions:
def is_list1_empty(list):
    if len(list)==0:
        #returning true as length is 0
        return True
    ## returning false as length is greater than 0
    return False

#passing parameters
list2=[1,2,3,4,5]
list1=[]
print(is_list1_empty(list1))
print(is_list1_empty(list2))
