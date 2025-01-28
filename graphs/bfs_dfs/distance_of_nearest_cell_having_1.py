from collections import deque
from copy import deepcopy

graph = [[0,0,0],[0,1,0],[1,0,1]]

def find_distance(graph):
    # TC: O(nm + 4nm), SC: O(3nm)
    n, m = len(graph), len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    dist = deepcopy(graph)
    q = deque()

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 1:
                q.append((r, c, 0))
                vis[r][c] = 1

    while q:
        row, col, steps = q.popleft()
        dist[row][col] = steps
        for dr, dc in [(0,-1), (-1,0), (0,1), (1,0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]: 
                vis[nr][nc] = 1
                q.append((nr, nc, steps + 1))
    return dist
print(find_distance(graph))

