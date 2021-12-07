'''print('.......Find common element from 2 lists using python.......')
list1=[]
list2=[]
for i in range(0,4):
    l1 = int(input('enter numbers for l1:'))
    list1.append(l1)
for j in range(0,4):
    l2 = int(input('enter numbers for l2:'))
    list2.append(l2)
print(list1)
print(list2)
def common(list1,list2):
    c=[value for value in list1 if value in list2]
    return c
d=common(list1,list2)
print('the common elements in both list1 and list2 are',d)
'''
#res = list(set.intersection(*map(set, listA)))

class Common:
    def common_elements(self,list1,list2):
        self.list1=list1
        self.list2=list2
        c = [value for value in list1 if value in list2]
        return c
c=Common()
result=c.common_elements(list1=[1,2,3,6],list2=[5,6,1,8])
print('the common elements are:',result)


