#To sort (ascending and descending) a dictionary by value
dict3={}
for i in range (2):
    key_el=input('enter key {}:'.format(i))
    val_el = input('enter value {}:'.format(i))
    dict3[key_el] = val_el
print(dict3)

class sort:
    def dict1_sort(self,dict1):
        self.dict1=dict1
        return dict(sorted(dict1.items()))
c=sort()
result=c.dict1_sort({'c':100,'b':200})
print('result is',result)


