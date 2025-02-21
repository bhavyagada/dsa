grid = [[1,3,1],[1,5,1],[4,2,1]]
n, m = len(grid), len(grid[0])

def paths_recursion(row, col):
    if row == 0 and col == 0: return grid[row][col]
    if row < 0 or col < 0: return float('inf')
    up = grid[row][col] + paths_recursion(row-1, col)
    left = grid[row][col] + paths_recursion(row, col-1)
    return min(up, left)
print("recursion: ", paths_recursion(n-1, m-1))

def paths_memo(row, col, dp):
    if row == 0 and col == 0: return grid[row][col]
    if row < 0 or col < 0: return float('inf')
    if dp[row][col] != -1: return dp[row][col]
    up = grid[row][col] + paths_memo(row-1, col, dp)
    left = grid[row][col] + paths_memo(row, col-1, dp)
    dp[row][col] = min(up, left)
    return dp[row][col]
dp = [[-1 for _ in range(m)] for _ in range(n)]
print("memoization: ", paths_memo(n-1, m-1, dp))

def paths_tab():
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0: dp[row][col] = grid[row][col]
            else:
                up, left = float('inf'), float('inf')
                if row > 0: up = grid[row][col] + dp[row-1][col]
                if col > 0: left = grid[row][col] + dp[row][col-1]
                dp[row][col] = int(min(up, left))
    return dp[n-1][m-1]
print("tabulation: ", paths_tab())

def paths_optimal():
    prev = [0 for _ in range(m)]
    for row in range(n):
        curr = [0 for _ in range(m)]
        for col in range(m):
            if row == 0 and col == 0: curr[col] = grid[row][col]
            else:
                up, left = float('inf'), float('inf')
                if row > 0: up = grid[row][col] + prev[col]
                if col > 0: left = grid[row][col] + curr[col-1]
                curr[col] = int(min(up, left))
        prev = curr
    return prev[m-1]
print("space optimized: ", paths_optimal())


