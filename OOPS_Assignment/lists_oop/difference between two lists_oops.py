class Difference:
    def difference_list(self,list1,list2):
        self.list1=list1
        self.list2=list2
        difference=list(set(list1)-(set(list2)))
        return difference
c=Difference()
result=c.difference_list(list1=[1,2,3,4],list2=[1,2,9,8])
print('the difference is:',result)

