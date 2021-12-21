#A python program to copy an image file into another file.
f1=open('jk.jpg','rb')
f2=open('jn.jpg','wb')
bytes=f1.read()
f2.writes(bytes)
f1.close()
f2.close()
