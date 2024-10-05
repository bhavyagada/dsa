def search_2d_matrix(matrix, target):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target: return True
        elif matrix[row][col] < target: low = mid + 1
        else: high = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
found = search_2d_matrix(matrix, target)
print(found)
assert found == True
