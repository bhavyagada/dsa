from collections import deque
graph = [[0,1,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0],[1,1,0,1]]

def bfs(graph, row, col, vis, n, m):
    q = deque()
    q.append((row, col))
    vis[row][col] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in zip([-1,0,1,0], [0,1,0,-1]):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and graph[nr][nc] == 1:
                vis[nr][nc] = 1
                q.append((nr, nc))

def number_of_islands(graph):
    # optimal => TC: O(nm), SC: O(nm)
    n, m = len(graph), len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if not vis[r][c] and graph[r][c] == 1:
                bfs(graph, r, c, vis, n, m)
                cnt += 1
    return cnt
print(number_of_islands(graph))

