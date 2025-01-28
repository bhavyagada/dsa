graph = {1: [2,3], 2: [1,5], 3: [1,4,6], 4: [3], 5: [2,7], 6: [3,7], 7: [5,6]}

def dfs(node, parent, graph, vis):
    vis[node] = True
    for adj in graph[node]:
        if not vis[adj]:
            if dfs(adj, node, graph, vis):
                return True
        elif adj != parent:
            return True
    return False

def detect_cycle(graph):
    # TC: O(n + 2e) + O(n), SC: O(n)
    n = len(graph)
    vis = [False] * (n + 1)
    if dfs(1, -1, graph, vis): return True
    return False
print(detect_cycle(graph))

