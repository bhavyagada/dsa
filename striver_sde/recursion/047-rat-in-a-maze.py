def get_paths(r, c, n, vis, matrix, ans, path, directions):
    if (r, c) == (n-1, n-1): 
        ans.append(path[:])
        return

    for d, cell in directions.items():
        row, col = cell
        nr = r + row
        nc = c + col
        if nr >= 0 and nr < n and nc >= 0 and nc < n and not vis[nr][nc] and matrix[nr][nc] == 1:
            path += d
            vis[nr][nc] = 1
            get_paths(nr, nc, n, vis, matrix, ans, path, directions)
            path = path[:-1]
            vis[nr][nc] = 0

matrix = [[1, 0, 0, 0],
          [1, 1, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 1]]
n = len(matrix)
vis = [[0]*n for _ in range(n)]
directions = {'D': (1,0), 'L': (0,-1), 'R': (0,1), 'U': (-1,0)}
ans = []
get_paths(0, 0, n, vis, matrix, ans, "", directions)
print(ans)
assert ans == ["DDRDRR", "DRDDRR"]
