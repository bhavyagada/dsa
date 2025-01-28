graph = [['x','x','x','x','x'],['x','o','o','x','o'],['x','x','o','x','o'],['x','o','x','o','x'],['o','o','x','x','x']]

def dfs(row, col, graph, vis, n, m):
    vis[row][col] = 1
    for dr, dc in [(0,-1),(-1,0),(0,1),(1,0)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and graph[nr][nc] == "o":
            dfs(nr, nc, graph, vis, n, m)

def surrounded_regions(graph):
    # TC: O(nm), SC: O(nm)
    n, m = len(graph), len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    top, left = 0, 0
    bottom, right = n - 1, m - 1
    for i in range(left, right + 1):
        if graph[top][i] == "o":
            dfs(top, i, graph, vis, n, m)

    for i in range(top, bottom + 1):
        if graph[i][right] == "o":
            dfs(i, right, graph, vis, n, m)

    for i in range(right, left - 1, -1):
        if graph[bottom][i] == "o":
            dfs(bottom, i, graph, vis, n, m)

    for i in range(bottom, top - 1, -1):
        if graph[i][left] == "o":
            dfs(i, left, graph, vis, n, m)

    for r in range(n):
        for c in range(m):
            if graph[r][c] == "o" and not vis[r][c]:
                graph[r][c] = "x"
    return graph
print(surrounded_regions(graph))

