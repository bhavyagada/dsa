graph = {1: [2,3], 2: [5,6], 3: [1,4,7], 4: [3,8], 5: [2], 6: [2], 7: [3,8], 8: [4,7]}

def dfs(node, graph, vis, res):
    # optimal => TC: O(n)+O(2e), SC: O(n)
    vis[node] = True
    res.append(node)

    for adj in graph[node]:
        if not vis[adj]:
            dfs(adj, graph, vis, res)

n = 9
vis = [False] * (n + 1)
res = []
dfs(1, graph, vis, res)
print(res)

