def reverseString(s):
    reversedString = ""
    for char in s:
        reversedString = char + reversedString
    return reversedString

s = "srilekha"

print("The original string", s)
print("The reversed string is - ", reverseString(s))