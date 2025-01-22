mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 8

def search_element(mat, target):
    # optimal => TC: O(n+m), SC: O(1)
    n, m = len(mat), len(mat[0])
    row, col = 0, m - 1

    while row < n and col >= 0:
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            row = row + 1
        else:
            col = col - 1
    return False
print(search_element(mat, target))

