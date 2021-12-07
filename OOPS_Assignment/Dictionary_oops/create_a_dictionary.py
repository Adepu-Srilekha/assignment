'''dict3={}
for i in range (2):
    key_el=input('enter key {}:'.format(i))
    val_el = input('enter value {}:'.format(i))
    dict3[key_el] = val_el
print(dict3)'''
print('......create a dictionary using oops......')
class create:
    def create_dict(self):
        dict1={}
        for i in range(3):
            key_el = input('enter key {}:'.format(i))
            val_el = input('enter value {}:'.format(i))
            dict1[key_el] = val_el
        return dict1
c=create()
result=c.create_dict()
print('the dictionary is',result)
