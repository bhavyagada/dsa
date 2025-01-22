mat = [[1,3,5],[2,6,9],[3,6,9]]

def upper_bound(row, x, m):
    low, high = 0, m - 1
    ans = m
    while low <= high:
        mid = (low + high) // 2
        if row[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def countLessEqual(mat, x, n, m):
    cnt = 0
    for i in range(n):
        cnt += upper_bound(mat[i], x, m)
    return cnt

def find_median(mat):
    # optimal => TC: O(log(max)) + O(nlogm), SC: O(1)
    n, m = len(mat), len(mat[0])
    low, high = float('inf'), float('-inf')
    for i in range(n):
        low = min(low, mat[i][0])
        high = max(high, mat[i][m-1])

    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        cnt = countLessEqual(mat, mid, n, m)
        if cnt <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(find_median(mat))

