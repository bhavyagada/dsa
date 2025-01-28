graph = {1: [], 2: [], 3: []}
# graph = {1: [2], 2: [1], 3: []}

def dfs(node, graph, vis):
    vis[node] = True
    for adj in graph[node]:
        if not vis[adj]:
            dfs(adj, graph, vis)

def number_of_provinces(graph):
    # optimal => TC: O(n) + O(n+2e), SC: O(n)
    n = len(graph)
    vis = [False] * (n + 1) 
    cnt = 0
    for i in range(1, n + 1):
        if not vis[i]:
            cnt += 1
            dfs(i, graph, vis)
    return cnt
print(number_of_provinces(graph))

