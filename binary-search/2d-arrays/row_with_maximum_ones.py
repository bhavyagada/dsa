mat = [[1,1,1],[0,0,1],[0,0,0]]

def find_row(mat):
    # optimal => TC: O(nlogm), SC: O(1)
    n, m = len(mat), len(mat[0])
    cnt_max, idx = 0, -1

    for r in range(n):
        low, high = 0, m - 1
        lb = m
        while low <= high:
            mid = (low + high) // 2
            if mat[r][mid] >= 1:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        if m - lb > cnt_max:
            idx = r
            cnt_max = m - lb
    return idx
print(find_row(mat))

