triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle)

def path_recursion(row, col):
    if row == n-1: return triangle[row][col]
    down = triangle[row][col] + path_recursion(row+1, col)
    diag = triangle[row][col] + path_recursion(row+1, col+1)
    return min(down, diag)
print("recursion: ", path_recursion(0, 0))

def path_memo(row, col, dp):
    if row == n-1: return triangle[row][col]
    if dp[row][col] != -1: return dp[row][col]
    down = triangle[row][col] + path_memo(row+1, col, dp)
    diag = triangle[row][col] + path_memo(row+1, col+1, dp)
    dp[row][col] = min(down, diag)
    return dp[row][col]
dp = [[-1 for _ in range(n)] for _ in range(n)]
print("memoization: ", path_memo(0, 0, dp))

def path_tab():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): dp[n-1][i] = triangle[n-1][i]

    for row in range(n-2, -1, -1):
        for col in range(row, -1, -1):
            dp[row][col] = triangle[row][col] + min(dp[row+1][col], dp[row+1][col+1])
    return dp[0][0]
print("tabulation: ", path_tab())

def path_optimal():
    # TC: O(n^2), SC: O(n)
    prev = [0 for _ in range(n)]
    for i in range(n): prev[i] = triangle[n-1][i]

    for row in range(n-2, -1, -1):
        curr = [0 for _ in range(row+1)]
        for col in range(row, -1, -1):
            curr[col] = triangle[row][col] + min(prev[col], prev[col+1])
        prev = curr
    return prev[0]
print("space optimized: ", path_optimal())


