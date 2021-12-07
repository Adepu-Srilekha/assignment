class Dict4:
    def __init__(self,dict1):
        self.dict1=dict1
    def check_key(self,x):
        if x in dict1:
            print('Key is present in the dictionary')
        else:
            print('Key is not present in the dictionary')

dict1 = {'nikhil': 40, 'asha': 2, 'bavana': 1, 'disha': 3, 'Nishi': 28, 'priya': 30}
x='nikhil'
obj=Dict4(dict1)
result=obj.check_key(x)
