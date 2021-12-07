class Swap:
    def swapping_string(self,str1):
        self.str1=str1
        start = str1[0]
        end = str1[-1]
        swapping_str = end + str1[1:-1] + start
        return (swapping_str)

str1 = "my name is srilekha"
s=Swap()
swap=s.swapping_string(str1)
print("the swapping of first and last character is :",swap)