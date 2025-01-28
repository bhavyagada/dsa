from collections import deque

graph = [[0,0,0,1,1],[0,0,1,1,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,0,1,1]]

def number_of_enclaves(graph):
    # TC: O(4nm), SC: (nm)
    n, m = len(graph), len(graph[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    top, left = 0, 0
    bottom, right = n - 1, m - 1

    q = deque()

    for i in range(left, right + 1):
        if graph[top][i] == 1 and not vis[top][i]:
            vis[top][i] = 1
            q.append((top, i))

    for i in range(top, bottom + 1):
        if graph[i][right] == 1 and not vis[i][right]:
            vis[i][right] = 1
            q.append((i, right))

    for i in range(right, left - 1, -1):
        if graph[bottom][i] == 1 and not vis[bottom][i]:
            vis[bottom][i] = 1
            q.append((bottom, i))

    for i in range(bottom, top - 1, -1):
        if graph[i][left] == 1 and not vis[i][left]:
            vis[i][left] = 1
            q.append((i, left))

    while q:
        r, c = q.popleft()
        for dr, dc in [(0,-1),(-1,0),(0,1),(1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and graph[nr][nc] == 1:
                vis[nr][nc] = 1
                q.append((nr, nc))

    cnt = 0
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            if not vis[r][c] and graph[r][c] == 1:
                cnt += 1
    return cnt
print(number_of_enclaves(graph))

