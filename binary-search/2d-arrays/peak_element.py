mat = [[10,20,15],[21,30,14],[7,16,32]]

def find_max(mat, col, n):
    row_idx = -1
    maxi = float('-inf')
    for i in range(n):
        if mat[i][col] > maxi:
            maxi = mat[i][col]
            row_idx = i
    return row_idx

def find_peak_element(mat):
    # optimal => TC: O(nlogm), SC: O(1)
    n, m = len(mat), len(mat[0])
    low, high = 0, m - 1
    while low <= high:
        mid = (low + high) // 2
        row = find_max(mat, mid, n)
        left = right = -1
        if mid - 1 >= 0:
            left = mat[row][mid - 1]
        if mid + 1 < n:
            right = mat[row][mid + 1]
        if mat[row][mid] > left and mat[row][mid] > right:
            return [row, mid]
        elif mat[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return None # dummy statement
print(find_peak_element(mat))

