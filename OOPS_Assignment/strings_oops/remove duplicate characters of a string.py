'''OrderedDict is a dictionary subclass that remembers the order of the keys that were inserted
first. Since there can't be duplicate keys this method will return the string after removing the duplicate
characters.'''
from collections import OrderedDict
class A:
    def remove_duplicate(self,str1):
        self.str1=str1
        return "".join(OrderedDict.fromkeys(str1))

str1="abcfgbsca"
print(str1)
b=A()
result=b.remove_duplicate(str1)
print("After removing duplicates: ",result)