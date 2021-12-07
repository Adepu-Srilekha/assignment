set1={1,2,3}
print(type(set1))
class Union1:
    def union_set(self,set1,set2):
        self.set1=set1
        self.set2=set2
        return set1.union(set2)
c=Union1()
result=c.union_set(set1={1,2,3},set2={4,5,6})
print(result)