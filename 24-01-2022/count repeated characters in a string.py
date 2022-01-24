string = 'Pythonn Programmming'
dictionary = {}
for char in string:
    if char in (dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char]=1
for char in dictionary:
    print(char,' -> ',dictionary[char])