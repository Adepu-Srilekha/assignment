from numpy import *
#creating a 3D array with size 2x2x3
a=[[[1,2,3],
    [4,5,6]],
   [[7,8,9],
    [10,11,12]]]
#display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end='\t')
        print()
    print()