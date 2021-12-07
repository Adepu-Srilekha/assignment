print('............remove odd index using oops.......')
class Odd:
    def remove_odd(self,result):
        self.result=result
        for i in range(len(string1)):
            if i%2!=0:
                result=result+string1[i]
        return result
string1=input('enter the string:')
c=Odd()
res=c.remove_odd(string1)
print('the result is:',res)