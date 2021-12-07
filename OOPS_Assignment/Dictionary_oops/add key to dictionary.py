#add key
dict1={'a':1,'b':2}
#dict1.update(c=2)
print(dict1)
dict1={'a':1,'b':2,}
#dict1.update(c='python')
#print(dict1)
dict1['d']='python'
print(dict1)
print('.........add key to dictionary using oops.......')
class Add:
    def add_key(self,dict1):
        self.dict1=dict1
        dict1['c']=57
        return dict1
c=Add()
result=c.add_key(dict1={'a':1,'b':5})
print('the result is:',result)
