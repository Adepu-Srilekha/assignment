print('capitalize the string using oops')

string1=('python')
class Capital:
    def capitalize(self,string1):
        self.string1=string1
        result=string1.capitalize()
        return result
c=Capital()
result2=c.capitalize(string1)
print('the result is',result2)
