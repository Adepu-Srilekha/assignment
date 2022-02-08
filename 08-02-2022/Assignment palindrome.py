from itertools import  permutations
def check_palindrome(str1):
    str2=str1[::-1]
    if str1==str2:
        return True
    else:
        return False