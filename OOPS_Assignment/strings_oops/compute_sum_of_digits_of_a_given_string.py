
class Sumdigit:
    def sum_digits(self,str1):
        self.str1=str1
        digit=0
        for i in str1:
            if i.isdigit()==True:
                a=int(i)
                digit=digit+a
        return digit
b=Sumdigit()
result=b.sum_digits(str1=('njnk8098j'))
print('the result is',result)
#the output is 25 because....8+0+9+8

