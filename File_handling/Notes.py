'''Data  is very important. Every organization depends on its data
for continuing its business operations.


Types of files in python:

Text files: store the data in the form of characters.
eg:python stored as 6 characters,expenses :2000 stores as 4 characters.

Binary files:stores the entire data in form of bytes.


opening a file:

file handler=open('file name','open mode','buffering')

file  name represents the name on which file the data is stored.

open mode represents the purpose of opening the file.


buffering represents a temporary block of memory,it is optional and used to set the size of the
buffer for the file..
Default buffer size is 4096 to 8192 bytes.


File operations:
1.Open a file
2.Read or Write(perform operation)
3.Close the file

Python File modes:
'r'---- Open a file for reading(default)we can choose (encoding='utf-8')
'w'----open a file for writing
'x'--- open a file for exclusive operation.If the
file already exists,the operation fails.
'a'----Open for appending the data at then end of the file
't'---- open in text mode
'b'---- open in binary  mode
'+'---- open a file for updating(reading and writing)
w+ ---- To read and write data of a file.The previous data in the file will be deleted
r+ ---- To read and write data of a file. The previous data in the fill not be deleted.
a+ --- to append and read data of a file
#If you want to store data longer period and simpler format the best way is text format
#to open the file, and need to mention for what purpose'''
f=open('Mydata','r')
print(f)
#how to fetch the data ...using read
print(f.read())
print(f.read(4))#only first  4 characters it prints
print(f.read(10))#it starts printing from the 4th to the 10 characters
f.tell()#tells whats the current cursor location
#if we want to move cursor back
f.seek(0)#it brings the cursor to initial position
#what if.. if we want to get only some part of data

#if suppose we are having huge data, we can pick whatever the data
#we require using the above..f.read(),f.tell(),f.seek()
print(f.readline())
#it only prints the first line
#if we want to print second line
print(f.readline())
print(f.readline())