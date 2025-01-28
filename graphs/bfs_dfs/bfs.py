from collections import deque

graph = {1: [2,6], 2: [1,3,4], 3: [2], 4: [2,5], 5: [4,8], 6: [1,7,9], 7: [6,8], 8: [5,7], 9: [6]}

def bfs_traversal(start):
    # optimal => TC: O(n)+O(2e), SC: O(n)
    n = 9
    bfs = []
    vis = [False] * (n + 1)
    q = deque()
    q.append(start)
    vis[start] = True

    while q:
        node = q.popleft()
        bfs.append(node)
        for adj in graph[node]:
            if not vis[adj]:
                q.append(adj)
                vis[adj] = True
    return bfs
print(bfs_traversal(1))

