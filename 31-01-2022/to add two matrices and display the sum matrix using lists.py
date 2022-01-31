#A python program to add two matrices and display sum matrix using lists.
#taking 1 matrix with 3 rows and 4 columns
m1=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,0]]

#taking 2nd matrix with 3 rows and 4 columns

m2=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,0]]


m3=[4*[0] for i in range(3)]
#taking 3rd matrix with 4 columns and 3 rows and initialize with 0
#adding corresponding elements of m1 and m2 and storing it into m3
for i in range(3):
    for j in range(4):
        m3[i][j]=m1[i][j]+m2[i][j]

#displaying third matrix using for loop
for i in range(3):
    for j in range(4):
        print(m3[i][j],end=' ')
    print()

