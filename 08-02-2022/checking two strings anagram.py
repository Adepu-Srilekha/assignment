string1 = "skyis"
string2 = "ssyki"
# converting the both strings to lowercase using lower() function.
string1 = string1.lower()
string2 = string2.lower()
# checking if both the strings are equal using sorted() function
if(sorted(string1) == sorted(string2)):
    print("Both the strings are anagrams")
else:
    print("Both the strings are not anagrams")