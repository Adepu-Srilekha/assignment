'''OS (Operating System) module is useful to perform several operations on directories
                    -> to find current working directory
                    -> changing to a particular directory
                    -> renaming a directory
                    -> deleting a directory
                    -> listing the contents of a directory
-> system() method of os module is useful to run commands or executable programs from our
Python programs.'''


#initially we are checking the file exists ...then read data
import os,sys

#opening the file for reading data

fname=input('enter filename:')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname,'does not found')
    sys.exit()

#if we dont give sys.exit() it prints the next statement also.
#read strings from the file
print('the file contents are:')
string1=f.read()
print(string1)

f.close()

