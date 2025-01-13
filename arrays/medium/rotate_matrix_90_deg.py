matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate_matrix(matrix):
    # optimal => TC: (2n^2), SC: O(1)
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for r in range(n):
        matrix[r].reverse()
rotate_matrix(matrix)
print(matrix)
