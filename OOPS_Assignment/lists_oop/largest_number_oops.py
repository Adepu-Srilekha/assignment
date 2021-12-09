list1 = [1, 2, 3, 4, 5, 6]
class largest:
    def myMax(self,list1):
        self.list1=list1
        max=list1[0]
        for x in list1:
            if x > max:
                max = x
        return max
c=largest()
result=c.myMax(list1)
print(result)