#program to sort words in alphabetical order:

string1 = input('Enter a string:')

words = [word.lower () for word in string1.split ()]

words.sort ()

print ('The words sorted in alphabetical order are as follows: ')
for word in words:
    print (word)