from collections import deque
graph = {1: [2,3], 2: [1,5], 3: [1,4,6], 4: [3], 5: [2,7], 6: [3,7], 7: [5,6]}

def bfs(src, graph, vis):
    # optimal => TC: O(n + 2e), SC: O(n)
    vis[src] = True
    q = deque()
    q.append((src, -1))

    while q:
        node, parent = q.popleft()
        for adj in graph[node]:
            if not vis[adj]:
                vis[adj] = True
                q.append((adj, node))
            elif parent != adj:
                return True
    return False

def detect_cycle(graph):
    n = len(graph)
    vis = [False] * (n + 1)
    for i in range(1, n + 1):
        if not vis[i]:
            if bfs(i, graph, vis): return True
    return False
print(detect_cycle(graph))

