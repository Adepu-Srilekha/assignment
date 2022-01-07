#Find all the values in a list are greater than a specified number
#for suppose we give a list ...list1=[1,2,3,4,5]
#the specified number is 3.. so print all the elements greater than 3
# than val using traversal

def check(list1, val):
    # traverse in the list
    for x in list1:

        # compare with all the values
        # with val
        if val <= x:
            yield x
list1 =[1,2,3,4,5,6,7]
val = 5
obj = check(list1, val)
'''print(obj)
print(next(obj))'''
for each in obj:
    print(each)