# taking a string which stores all the punctuations and
# initialize it with some punctuations
punctuationString = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# given string which we want  to remove the punctuation marks
given_string = "BTechGeeks, is best: for !Python.?[]() ;"
# Taking a empty which stores all the characteers of original string without punctuations
noPunctuationString = ""
# removing all punctuations from the string
# Traversing the original string
for character in given_string:
  # if character not in punctuationString which means it is not a punctuation
  # hence concate this character to noPunctuationString
    if character not in punctuationString:
        noPunctuationString = noPunctuationString + character
# printing the given string after removing the punctuations
print("printing the given string after removing the punctuations : ")
print(noPunctuationString)