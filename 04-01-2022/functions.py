#parameters:

def wish(name):
    print('hello',name)
print(wish('srilekha'))
wish('lekha')


#write a function to take number as input and print its square value.
def square(n):
    print('the square of a number is:')
    return n*n
result=square(4)
print(result)


#write a function to accept 2 numbers as input and return sum.
def add(a,b):
    c=a+b
    return c
result1=add(5,6)
print(result1)
#If we are not writing return statement then default return value is none.



#Default arguements
#sometimes we can provide default values to our positional arguements.
def wish(name='srilekha'):
    print('hello',name,'good morning')
wish('lekha')
wish()#not passing any name then only default value will be considered.

#variable Length arguements:
# we can declare a variable length arguement with *symbol
def sum(*n):
    total=0
    for n1 in n:
        total+=n1
        print('the sum is:',total)
sum()
sum(10,20)

