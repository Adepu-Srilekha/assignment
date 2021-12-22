'''Array:
Array is a collection of elements(or values) of same datatype.
--- can store only integer type elements
--- can store only float type elements
--- cannot store one integer,one float and one character type element in the same array
--- can increase or decrease the size dynamically,we need not declare


Advantages of array:
--- similar to lists.. the difference is list can store multiple data types where as array cannot
--- less memory than lists and offer faster execution than lists
---  need to specify how many elements we are going to enter
--- useful to handle colletion of elements
---- methods useful to process array elements of any array are available in 'array' module.'''


#3 ways to import arrays:
import array

a=array.array('i',[1,2,3,4,5])

import array as ar

a=ar.array('i',[1,2,3,4,5])

from array import*
a=array('i',[1,2,3,4,5])



#creating an array whose name is (variable name) and with integer type elements

#A python program to create an integer type array.
from array import*
a = array('i',[2,3,4,7,8])
print('the array elements are:')
for elements in a:
    print(elements)
