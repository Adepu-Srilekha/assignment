#create a list with squares of integers from 1 to 10
squares=[]
for x in range(1,11):
    squares.append(x**2)
print(squares)

#if we want to get squares of integers from 1 to 10 and take only the even numbers from the result..
even_squares=[x**2 for x in range(1,10) if x%2==0]
print(even_squares)