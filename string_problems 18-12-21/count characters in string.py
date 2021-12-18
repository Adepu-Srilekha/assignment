#count characters in string
input_string='strings are immutable'
print(input_string.count('are'))


#using for loop
input_string='strings are immutable'
print('........using for loop....')
word='are'
for i in input_string.split():
    if i==word:
        print(input_string.count(word))
