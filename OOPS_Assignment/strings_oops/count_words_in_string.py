#using built in functions
str = input("Enter the string:")
print(str.count("is"))
#using oops
print('counting the words in the strings using oops')
class Counting:
    def count1(self,string1,word1):
        self.string1=string1
        self.word1=word1
        for element in string1.split():
            if element==word1:
                pass
        #print(string1.count(word1))
        return string1.count(word1)
string1=input('enter a string:')
word1=input('enter the word to count:')
b=Counting()
result1=b.count1(string1,word1)
print('the no.of words are:',result1)

