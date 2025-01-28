graph = {1:[2], 2: [3], 3: [4,7], 4: [5], 5: [6], 6: [], 7: [5], 8: [2,9], 9: [10], 10: [8]}

def dfs(node, graph, vis, path_vis):
    vis[node] = 1
    path_vis[node] = 1

    for adj in graph[node]:
        if not vis[adj]:
            if dfs(adj, graph, vis, path_vis):
                return True
            elif path_vis[adj]:
                return True
    path_vis[node] = 0
    return False

def detect_cycle(graph):
    # TC: O(n+e), SC: O(n)
    n = len(graph)
    vis = [0] * (n + 1)
    path_vis = [0] * (n + 1)

    for i in range(1, n + 1):
        if not vis[i]:
            if dfs(i, graph, vis, path_vis):
                return True
    return False
print(detect_cycle(graph))

