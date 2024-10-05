def setZeros(matrix):
    n, m = len(matrix), len(matrix[0])
    col0 = 1
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                if c != 0: matrix[0][c] = 0
                else: col0 = 0
    
    for r in range(1, n):
        for c in range(1, m):
            if matrix[r][c] != 0:
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for c in range(1, m): matrix[0][c] = 0

    if col0 == 0:
        for r in range(n): matrix[r][0] = 0

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeros(matrix1)
assert matrix1 == [[1,0,1],[0,0,0],[1,0,1]]
setZeros(matrix2)
assert matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]