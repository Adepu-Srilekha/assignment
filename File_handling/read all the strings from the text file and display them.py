f1=open('textfile.txt','r')
print('the file contents are:')
#reading the strings from the file
string1=f1.read()
print(string1)



#using for loop to read line by line from the file
for line in f1:
    print(line)
