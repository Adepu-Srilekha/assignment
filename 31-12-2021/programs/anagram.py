'''Two strings can be called Anagram if the same character with the same occurrence,
present in both string. In this case position of characters not matters.

For eg:  “quescol” and “colsque” both strings are anagram. As you can see here, both the string
have same character with same time of occurrence at different position and it is an anagram.

But if we take another example like “love” and “like”. In the both string only two character
‘l’ and ‘e’ are common and rest are not. So this two strings are not an anagram.'''


def anagramCheck(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if anagramCheck(str1, str2):
    print("Anagram")
else:
    print("Not an anagram")