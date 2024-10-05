def rotate_image(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for r in range(n):
        matrix[r].reverse()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_image(matrix)
print(matrix)
assert matrix == [[7,4,1],[8,5,2],[9,6,3]]
