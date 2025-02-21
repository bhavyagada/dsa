matrix = [[2,1,3],[6,5,4],[7,8,9]]
n = len(matrix)

def path_sum_recursion(row, col):
    if col < 0 or col >= n: return float('inf')
    if row == 0: return matrix[0][col]
    return matrix[row][col] + min(path_sum_recursion(row-1, col-1), path_sum_recursion(row-1, col), path_sum_recursion(row-1, col+1))
res = min(path_sum_recursion(n-1, col) for col in range(n))
print("recursion: ", res)

def path_sum_memo(row, col, dp):
    if col < 0 or col >= n: return float('inf')
    if row == 0: return matrix[0][col]
    if dp[row][col] != -1: return dp[row][col]
    dp[row][col] = matrix[row][col] + min(path_sum_memo(row-1, col-1, dp), path_sum_memo(row-1, col, dp), path_sum_memo(row-1, col+1, dp))
    return dp[row][col]
dp = [[-1 for _ in range(n)] for _ in range(n)]
res = min(path_sum_memo(n-1, col, dp) for col in range(n))
print("memoization: ", res)

def path_sum_tab():
    # TC: O(n^2) + O(n), SC: O(n^2)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0] = matrix[0]
    for row in range(1, n):
        for col in range(n):
            up = dp[row-1][col]
            ld, rd = float('inf'), float('inf')
            if col-1 >= 0: ld = dp[row-1][col-1]
            if col+1 < n: rd = dp[row-1][col+1]
            dp[row][col] = matrix[row][col] + int(min(up, ld, rd))
    return min(dp[n-1])
print("tabulation: ", path_sum_tab())

def path_sum_optimal():
    # TC: O(n^2) + O(n), SC: O(n)
    prev = matrix[0]
    for row in range(1, n):
        curr = [0 for _ in range(n)]
        for col in range(n):
            up = prev[col]
            ld, rd = float('inf'), float('inf')
            if col-1 >= 0: ld = prev[col-1]
            if col+1 < n: rd = prev[col+1]
            curr[col] = matrix[row][col] + int(min(up, ld, rd))
        prev = curr
    return min(prev)
print("space optimized: ", path_sum_optimal())


