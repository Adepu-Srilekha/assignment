#example
#import module sys to get the type of the exception
import sys
lst=['b',0,2]
#here we can divide 1/2 but dividing 1/b and 1/0 are exceptions
for entry in lst:
    try:
        print('the entry is:',entry)
        a=1 / int(entry)
#here the first value is b,we cannot do 1/b it raises an error and
#jumps  to except block
#errors are handled gracefully in except block.
#sys.exc_info()....it gives the type of the error occured
    except:
        print(sys.exc_info()[0],'occured')
        print('next entry')
print('the reciprocal of ',entry,'is',a)
#whenever we doesn't raise error in try block,except block is not executed
#and directly comes to the last statement.



#if we want execute our program based on errors




lst=['b',0,2]

for entry in lst:
    try:
        print('the entry is',entry)
        a= 1 / int(entry)
    except(ValueError):
        print('this is a value error')
    except(ZeroDivisionError):
        print('this is a zerodivision error')
    except:
        print('some other error')
print('the reciprocal of',entry,'is', a)


#if    try
#elif except
#elif  except
#else  finally

#these are multiple exception blocks
#except block is also called catch block
#in this case the error is raised by the interpreter..


'''#we can also RAISE EXCEPTIONS:

raise KeyboardInterrupt
raise MemoryError'''

print('raising the error and handling the error')
try:
    num=int(input('enter a positive number:'))
    if num<=0:
        raise ValueError('Error:Entered negative number')
except ValueError as e:
    print(e)
#it is going to give the error but doesnt stop

#try and finally:
#finally is written and run at the end of all blocks.
try:
    f=open(filename)
    #perform operations here
finally:
    f.close()


