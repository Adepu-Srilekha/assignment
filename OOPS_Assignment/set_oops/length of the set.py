print('.......length of the set using oops..............')
class Length:
    def length_set(self,name_input):
        self.name_input=name_input
        total=0
        for res in name_input:
            total=total+1
        return total
name=input('enter a string:')
c=Length()
result=c.length_set(name)
print('the length of the set is:',result)
