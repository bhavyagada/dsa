graph = {1: [2], 2: [1,3,6], 3: [2,4], 4: [3,5,7], 5: [4,6], 6: [2,5], 7: [4,8], 8: [7]}

def dfs(node, graph, color, next_color):
    color[node] = next_color
    for adj in graph[node]:
        if color[adj] == -1:
            if not dfs(adj, graph, color, 1 - next_color):
                return False
        elif color[adj] == next_color:
            return False
    return True

def is_bipartite(graph):
    # TC: O(n+2e), SC: O(n)
    n = len(graph)
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(i, graph, color, 0): 
                return False
    return True
print(is_bipartite(graph))

