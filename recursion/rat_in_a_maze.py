mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

def find_paths(row, col, n, mat, vis, path, res):
    # TC: O(4^(n*n)), SC: O(n*n)
    if row == n-1 and col == n-1:
        res.append(path)
        return

    for i, j, p in [(1,0,"D"), (0,-1,"L"), (0,1,"R"), (-1,0,"U")]:
        ni, nj = row + i, col + j
        if 0 <= ni < n and 0 <= nj < n and not vis[ni][nj] and mat[ni][nj] == 1:
            vis[row][col] = 1
            find_paths(ni, nj, n, mat, vis, path+p, res)
            vis[row][col] = 0

res = []
n = len(mat)
vis = [[0 for _ in range(n)] for _ in range(n)]
find_paths(0, 0, n, mat, vis, "", res)
print(res)

