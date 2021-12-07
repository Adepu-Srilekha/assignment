list1=[1,2,3,4,5]
class Multiply:
    def sums(self,list1):
        self.list1=list1
        num=1
        for i in list1:
            num=num*i
        return num
c=Multiply()
result=c.sums(list1)
print('multiplication of elements is:',result)

