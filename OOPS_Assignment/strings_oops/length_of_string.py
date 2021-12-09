class Length:
    def str_len(self,name):
        self.name=name
        total=0
        for res in name:
            total = total+1
        return total
name = input("enter the String:")
a=Length()
result=a.str_len(name)
print('length of the total string is',result)