matrix = [[1,1,1],[1,0,1],[1,1,1]]

def set_zero_better(matrix):
    # better => TC: O(2nm), SC: O(n+m)
    n, m = len(matrix), len(matrix[0])
    row = [0] * n
    col = [0] * m

    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0:
                row[r] = 1
                col[c] = 1
    
    for r in range(n):
        for c in range(m):
            if matrix[r][c] != 0 and (row[r] == 1 or col[c] == 1):
                matrix[r][c] = 0
set_zero_better(matrix)
print("set matrix zero (better)", matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def set_zero_optimal(matrix):
    # optimal => TC: O(2nm), SC: O(1)
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
        for c in range(m): matrix[0][c] = 0
    
    if col0 == 0:
        for r in range(n): matrix[r][0] = 0

set_zero_optimal(matrix)
print("set matrix zero (optimal)", matrix)
