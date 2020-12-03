matrix =  [ [ 1, 1, 0, 0, 1, 1 ],
            [ 0, 0, 1, 0, 1, 1 ],
            [ 1, 1, 1, 1, 1, 0 ],
            [ 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1 ],
            [ 0, 1, 1, 1, 1, 1 ],
            [ 1, 0, 0, 0, 1, 1 ]]
table = [[0]*len(matrix[0])]*len(matrix)
r = len(matrix)
c = len(matrix[0])
max_size = 0
for i in range(r):
    for j in range(c):
        if(i == 0 or j == 0):
            #print(i,j)
            table[i][j] = matrix[i][j]
            max_size = table[i][j] if table[i][j] > max_size else max_size
        elif(matrix[i][j] == 0):
            table[i][j] = 0
        else:
            table[i][j] = min(table[i-1][j],table[i][j-1],table[i-1][j-1]) + 1
            max_size = table[i][j] if table[i][j] > max_size else max_size
print(table)
print(max_size)