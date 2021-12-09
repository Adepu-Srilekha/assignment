#max_len=0
#for ele in list_string1:
 #   if len(ele)>max_len:
  #      max_len=len(ele)
   #     result=ele
#print(result)
print('length of longest string using oops')
class Longest:
    def longest_string(self,list_string1):
        self.list_string1=0
        max_len=0
        for ele in list_string1 :
            if len(ele)>max_len:
                max_len=len(ele)
                result=ele
        return ele
d=Longest()
result1=d.longest_string(list_string1 =['python','learning','technology'])
print('the longest string is',result1)
#if we want to take the input from the user:
str1=[]
for i in range(4):
    str2=input('enter the string:')
    str1.append(str2)
