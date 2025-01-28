from copy import deepcopy

graph = [[1,1,1],[1,1,0],[1,0,1]]

def dfs(row, col, ans, graph, new_color, init_color, n, m):
    ans[row][col] = new_color
    for dr, dc in zip([-1,0,1,0], [0,1,0,-1]):
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == init_color and ans[nr][nc] != new_color:
            dfs(nr, nc, ans, graph, new_color, init_color, n, m)

def flood_fill(graph, new_color):
    # optimal => TC: O(nm + 4nm), SC: O(nm)
    n, m = len(graph), len(graph[0])
    sr, sc = 1, 1
    init_color = graph[sr][sc]
    ans = deepcopy(graph)
    dfs(sr, sc, ans, graph, new_color, init_color, n, m)
    return ans
print(flood_fill(graph, 2))

