X = [[1,4,5], [3,7,9]]

result = [[0,0],[0,0], [0,0]]
print(len(X))
print(len(X[0]))
for i in range (len (X)): #len(x)---2
    for j in range (len (X[0])): #len(x[0])----3
        result [j][i] = X [i][j]

for r in result:
    print (r)