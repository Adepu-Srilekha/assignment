print('...reverse a string if its length is multiple of 4....')
class Reverse:
    def reverse_string(self,str1):
        self.str1=str1
        if len(str1) % 4 == 0:
            return ''.join(reversed(str1))
        return str1
c=Reverse()
result=c.reverse_string(str1='ghjk')z
print('the result is',result)
