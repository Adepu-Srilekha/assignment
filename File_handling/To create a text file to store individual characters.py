#Here we are storing so we need to write mode
#creating a file to store characters.
f1=open('textfile.txt','w')
string1=input('enter text:')

#writing the string1 to the file f1
f1.write(string1)



#If we run again,already entered data in the file is lost and the file will be created
#as fresh file without any data.



#if we want to retain the previous data and add the new data at end end of the file.
#create a new file and specify the method append
#f1=open('textfile.txt','r')
#this will read the data from f1 and returns them into the string
#string2=f1.read()
#print(string1)
#f1.close()

