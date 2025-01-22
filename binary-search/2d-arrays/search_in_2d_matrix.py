mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def search_element(mat, target):
    # optimal => TC: O(log(nm)), SC: O(1)
    n, m = len(mat), len(mat[0])
    low, high = 0, n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(search_element(mat, 8))

