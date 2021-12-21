'''Data stored on a secondary storage media like hard disk or CD is called a file.
-> Once the data stored in a file, the same data can be shared by several programs.
-> There are two types of files supported by Python: text files and binary files
                    -> Text files store data in the form of text or characters.
                    -> Binary files store data in the form of bytes.
-> The open() method opens a file for some operation like writing, reading or appending.
-> The close() method closes a file.
-> The read() method reads the file content.
-> The write() method stores the data into file.
-> For binary files we have to add 'b' at the end of file open mode.
-> 'wb' represents write mode for a binary file.
-> Binary files are useful to handle text files, image or audio or video files.
-> We need not close the file if we open the file using 'with' statement.
-> Pickle or Serialization is process of storing objects into binary file.
-> Unpicke or de-serialization is a process retrieving objects from a binary file.
-> Pickle use dump() method
-> Unpickle use load() method.
-> In a binary file, to know the position of file pointer, we can use tell() method.
-> In a binary file, to move the file pointer to any position, we can use seek() method.
-> encode() method converts string into bytes so that it can be written into a binary file.
-> Binary string can be converted into ordinary string using decode() method.
-> Random Accessing:-> Accessing a contents of a file randomly by moving a file pointer to any byte in the file.
                -> seek() and tell() methods.
                -> It is also possible using mmap(memory mapped file) module.
-> Zipping and Unzipping of files can be done using 'ZipFile' class of zipfile module.
-> OS (Operating System) module is useful to perform several operations on directories
                    -> to find current working directory
                    -> changing to a particular directory
                    -> renaming a directory
                    -> deleting a directory
                    -> listing the contents of a directory
-> system() method of os module is useful to run commands or executable programs from our Python programs.

"""
# to write in the file   -----> Overwrite the previous contents
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','w') # w-> it will create a new file if file is not present
string = input("Enter text:")
f.write(string)
f.close()

print("--------------------")

# to append the data in file  -----> Append the new contents at the end of the file
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','a') # a -> it will create a new file if file is not present
string = input("Enter text:")
f.write(string)
f.close()

print("--------------------")
# to read content in the file   -----> To read the contents of the file
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string1 = f.read()
print(string1)
f.close()

print("--------------------")
# to read limited content in the fie
f = open('C:\\Users\\Admin\\Desktop\\hello.txt','r')
string1 = f.read(22)       # -----> to read only 22 characters from file
print(string1)
f.close()'''