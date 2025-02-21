import time
grid = [[3,1,1], [2,5,1], [1,5,5], [2,1,1]]
n, m = len(grid), len(grid[0])

def pickup_recursion(row, c1, c2):
    # TC: O(3^n * 3^n), SC: O(n)
    if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m: return -1
    if row == n-1:
        if c1 == c2: return grid[row][c1]
        else: return grid[row][c1] + grid[row][c2]
    
    maxi = 0
    for dc1 in range(-1, 2):
        for dc2 in range(-1, 2):
            value = 0
            if c1 == c2: value = grid[row][c1]
            else: value = grid[row][c1] + grid[row][c2]
            value += pickup_recursion(row + 1, c1 + dc1, c2 + dc2)
            maxi = max(maxi, value)
    return maxi
print("recursion: ", pickup_recursion(0, 0, m-1))

def pickup_memo(row, c1, c2, dp):
    # TC: O(n*m*m) x 9, SC: O(n*m*m) + O(n)
    if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m: return -1
    if row == n-1:
        if c1 == c2: return grid[row][c1]
        else: return grid[row][c1] + grid[row][c2]
    if dp[row][c1][c2] != -1: return dp[row][c1][c2]
    maxi = 0
    for dc1 in range(-1, 2):
        for dc2 in range(-1, 2):
            value = 0
            if c1 == c2: value = grid[row][c1]
            else: value = grid[row][c1] + grid[row][c2]
            value += pickup_memo(row + 1, c1 + dc1, c2 + dc2, dp)
            maxi = max(maxi, value)
    dp[row][c1][c2] = maxi
    return dp[row][c1][c2]
dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
print("memoization: ", pickup_memo(0, 0, m-1, dp))

def pickup_tab():
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2: dp[n-1][j1][j2] = grid[n-1][j1]
            else: dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
    
    for row in range(n-2, -1, -1):
        for c1 in range(m):
            for c2 in range(m):
                maxi = 0
                for dc1 in range(-1, 2):
                    for dc2 in range(-1, 2):
                        value = 0
                        if c1 == c2: value = grid[row][c1]
                        else: value = grid[row][c1] + grid[row][c2]
                        if 0 <= c1+dc1 < m and 0 <= c2+dc2 < m: value += dp[row+1][c1+dc1][c2+dc2]
                        else: value += -1
                        maxi = max(maxi, value)
                dp[row][c1][c2] = maxi
    return dp[0][0][m-1]
print("tabular: ", pickup_tab())

def pickup_optimal():
    prev = [[0 for _ in range(m)] for _ in range(m)]
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2: prev[j1][j2] = grid[n-1][j1]
            else: prev[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
    
    for row in range(n-2, -1, -1):
        curr = [[0 for _ in range(m)] for _ in range(m)]
        for c1 in range(m):
            for c2 in range(m):
                maxi = -float('inf')
                for dc1 in range(-1, 2):
                    for dc2 in range(-1, 2):
                        value = grid[row][c1] if c1 == c2 else grid[row][c1] + grid[row][c2]
                        if 0 <= c1+dc1 < m and 0 <= c2+dc2 < m: value += prev[c1+dc1][c2+dc2]
                        else: value += -1
                        maxi = max(maxi, value)
                curr[c1][c2] = maxi
        prev = curr
    return prev[0][m-1]
print("space optimized: ", pickup_optimal())
