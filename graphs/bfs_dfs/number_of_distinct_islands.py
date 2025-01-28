graph = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]

def dfs(row, col, graph, vis, n, m, islands, row0, col0):
    vis[row][col] = 1
    islands.append((row - row0, col - col0))

    for dr, dc in [(-1,0),(0,-1),(1,0),(0,1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and graph[nr][nc] == 1:
            dfs(nr, nc, graph, vis, n, m, islands, row0, col0)

def number_of_distinct_islands(graph):
    # TC: O(nm + nm4), SC: O(nm)
    n, m = len(graph), len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(m)]
    st = set()

    for r in range(n):
        for c in range(m):
            if not vis[r][c] and graph[r][c] == 1:
                islands = []
                dfs(r, c, graph, vis, n, m, islands, r, c)
                st.add(tuple(islands))
    return len(st), st
print(number_of_distinct_islands(graph))


