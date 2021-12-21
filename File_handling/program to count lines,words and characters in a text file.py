import os,sys
fname = input('Enter file name:')

if os.path.isfile(fname):
    f1=open(fname,'r')


    cl=cw=cc=0
    for line in f1:
        cl+=1
        words=line.split()
        print(words)
        cw+= len(words)
        for char in words:
            cc+=len(char)

    print('total lines are:',cl)
    print('total words are:',cw)
    print('total characters:',cc)

else:
    print(fname,'not found')
    sys.exit()
