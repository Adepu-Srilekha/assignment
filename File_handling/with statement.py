'''with statement:
----can be used while opening a file
----takes care of closing a file which is opened by it.
syntax: with open('filename','open mode') as fileobject:'''



with open('textfile.txt','r') as f:
    print(f.read())



with open('textfile.txt','w') as f:
    print(f.write('I am learning\n'))
    print(f.write('python\n'))


#using for loop with:


#use 'with' to open a file and read data from it
with open('Mydata','r') as f1:
    for line in f1:
        print(line)