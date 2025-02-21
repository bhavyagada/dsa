grid = [[0,0,0],[0,1,0],[0,0,0]]

def unique_paths():
    # TC: O(n*m), SC: O(2m)
    n, m = len(grid), len(grid[0])
    prev = [0] * m
    for row in range(n):
        curr = [0] * m
        for col in range(m):
            if grid[row][col] == 1: curr[col] = 0
            elif row == 0 and col == 0: curr[col] = 1
            else:
                up, left = 0, 0
                if row > 0: up = prev[col]
                if col > 0: left = curr[col-1]
                curr[col] = up + left
        prev = curr
    return prev[m-1]
print(unique_paths())


