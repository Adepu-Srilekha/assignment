#Add member(s) in a set.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

set1={1,2,3,4,5,'apple','banana'}
set1.add(6)
print(set1)

print('.........add members to a set...............')
class Add:
    def add_set(self,set1):
        self.set1=set1
        set1.add(4)
        return set1
set1={1,2,5,6}
c=Add()
result=c.add_set(set1)
print('the result after adding the value is:',result)






