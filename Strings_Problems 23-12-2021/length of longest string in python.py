#length of longest string in python
string1 = input("Enter sentence : ")
lt3 = string1.split(" ")
max_length = 0
for i in lt3:
    if(max_length < len(i)):
        max_length = len(i)
print("Longest word length : ",max_length)