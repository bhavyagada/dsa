n = 3
m = 7

def path_recursion(row, col):
    # TC: O(2^(n*m)), SC: O((n-1)+(m-1))
    if row == 0 and col == 0: return 1
    if row < 0 or col < 0: return 0
    
    up = path_recursion(row-1, col)
    left = path_recursion(row, col-1)
    return up + left
print("recursion: ", path_recursion(n-1, m-1))

def path_memo(row, col, dp):
    # TC: O(n*m), SC: O(n*m) + O((n-1)+(m-1))
    if row == 0 and col == 0: return 1
    if row < 0 or col < 0: return 0
    if dp[row][col] != -1: return dp[row][col]

    up = path_memo(row-1, col, dp)
    left = path_memo(row, col-1, dp)
    dp[row][col] = up + left
    return dp[row][col]
dp = [[-1 for _ in range(m)] for _ in range(n)]
print("memoization: ", path_memo(n-1, m-1, dp))

def path_tab():
    # TC: O(n*m), SC: O(n*m)
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0: dp[0][0] = 1
            else:
                up, left = 0, 0
                if row > 0: up = dp[row-1][col]
                if col > 0: left = dp[row][col-1]
                dp[row][col] = up + left
    return dp[n-1][m-1]
print("tabulation: ", path_tab())

def path_space_optized():
    # TC: O(n*m), SC: O(m)
    prev = [0 for _ in range(m)]
    for row in range(n):
        curr = [0 for _ in range(m)]
        for col in range(m):
            if row == 0 and col == 0: curr[0] = 1
            else:
                up, left = 0, 0
                if row > 0: up = prev[col]
                if col > 0: left = curr[col-1]
                curr[col] = up + left
        prev = curr
    return prev[m-1]
print("space optimized: ", path_space_optized())

def path_optimal():
    dp = [1 for _ in range(m)]
    for _ in range(1, n):
        for col in range(1, m):
            dp[col] += dp[col-1]
    return dp[m-1]
print("optimal: ", path_optimal())


