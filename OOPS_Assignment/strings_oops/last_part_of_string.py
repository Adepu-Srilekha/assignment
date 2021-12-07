print('last part of the string using oops')
class Last:
    def last_part(self,list_strings):
        self.list_strings=list_strings
        for word in list_strings:
            if word==word[-1]:
                pass
            result=word
        return word
string1=[]
for i in range(4):
    str2=input('enter the string:')
    string1.append(str2)
c=Last()
result1=c.last_part(str2)
print('the last part of the string is :',result1)
