list1=[1,2,3,4,5,7]
class Sum:
    def sums(self,list1):
        self.list1=list1
        num=0
        for i in list1:
            num=num+i
        return num
c=Sum()
result=c.sums(list1)
print('the sum of elements is:',result)