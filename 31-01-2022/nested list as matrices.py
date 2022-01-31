#creating amatix with 3 rows and 3 columns.
mat=[[1,2,3],[4,5,6],[7,8,9]]
#to display row by row
for i in mat:
    print(i)
#to display each column in row 0:
for j in mat[0]:
    print(j,end=' ')
#to display each column in row 1:
for k in mat[1]:
    print(k,end=' ')
#to display each column in row 2:
for l in mat[2]:
    print(l,end=' ')
print()
#to get in next line we have used print() here
print("To Display all elements using for:")
for a in range(len(mat)):
    for b in range(len(mat[a])):
        print( mat[a][b],end=' ')
    print()
