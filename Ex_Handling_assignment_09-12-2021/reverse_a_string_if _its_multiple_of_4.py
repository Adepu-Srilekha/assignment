#reverses a string if it's length is a multiple of 4
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass



#reverse a string if it's length is a multiple of 4
#except block only executes if there is an error in try block
def reverse():
    try:
        string1 = int(input('enter a string:'))
        if len(string1) % 4 ==0:
            print(''.join(reversed(string1)))
    except Exception as e:
            print('the exception is',e)

reverse()


#find the maximum occurring character in a given string








