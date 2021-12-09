'''File operations:
1.Open a file
2.Read or Write(perform operation)
3.Close the file

Python File modes:
'r'---- Open a file for reading(default)we can choose (encoding='utf-8')
'w'----open a file for writing
'x'--- open a file for exclusive operation.If the
file already exists,the operation fails.
'a'----Open for appending at then end of the file
't'---- open in text mode
'b'---- open in binary  mode
'+'---- open a file for updating(reading and writing)

#If you want to store data longer period and simpler format the best way is text format
#to open the file, and need to mention for what purpose'''
f=open('Mydata','r')
print(f)
#how to fetch the data ...using read
print(f.read())
print(f.read(4))---only first  4 characters it prints
print(f.read(10))---it starts printing from the 4th to the 10 characters
f.tell()---#tells whats the current cursor location
#if we want to move cursor back
f.seek(0)--- #it brings the cursor to initial position
#what if.. if we want to get only som epart of data

#if suppose we are having huge data, we can pick whatever the data
#we require using the above..f.read(),f.tell(),f.seek()
print(f.readline())
#it only prints the first line
#if we want to print second line
print(f.readline())
print(f.readline())
#how to write data
f1=open('abc','w')
#it will create a file
#if we wants to write anything in the abc file
f1.write('python')
#if we want to append some text in abc file
f1=open('abc','a')
f1.write('hello world')
# we have 2 files here .. if we want to copy one file and store to other
f=open('Mydata','r')
f1=open('abc','w')
for data in f:
    f1.write(data)
#in files we have character mode and binary mode
#if we are using image data..wb means write binary
f=open('image file','wb')
for i in f:
    print(f.write(i))


'''Renaming and Deleting Files in Python:
first of all import os'''
import os
os.rename('test.txt','sample_txt')
#for deleting a file
os.remove('sample.txt')
#os is the module in which rename and remove functions exist




Python directory and File management:



