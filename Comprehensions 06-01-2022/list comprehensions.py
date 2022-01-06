#List comprehensions:
#comprehensions provide concise way to create lists,dict,sets.
#more compact and faster than normal functions for creating list
# reduce the no.of lines of code
#syntax:[expression for item in sequence <conditions>]

print('...using for loop...')
list1=[]
for letter in 'python': #iterating through sequence
    list1.append(letter)
print(list1)


print('using comprehension1')
list_comp1=[x for x in 'python']
print(list_comp1)


print('using comprehension2')
list_comp2=[x*x for x in range(10)]
print(list_comp2)

print('even numbers')
even=[]
list_even=[x for x in range(10) if x%2==0]
print(list_even)

print('odd numbers')
odd=[]
list_odd=[x for x in range(10) if x%2==1]
print(list_odd)


print('list comprehension with 2 if statements')
numbers=[]
list_if=[x for x in range(20) if x%2==0 if x%5==0]
print(list_if)

print('using sequence')
seq=[x*x*x for x in [1,2,3,4]]
print(seq)

print('for loop2')
old=[1,2,3,4,5,6]
new=[]
for item in old:
    if item in range(1,5):#upto range 5 only it appends
        new.append(item)
print(new)

print('using comprehension2')
old1=[1,2,3,4,5,6]
new1=[]
list_co=[item for item in old1 if item in range(1,5)]
print(list_co)
