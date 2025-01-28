from collections import deque

graph = {1: [2], 2: [1,3,6], 3: [2,4], 4: [3,5,7], 5: [4,6], 6: [2,5], 7: [4,8], 8: [7]}

def check(start, graph, color):
    # TC: O(n), SC: O(n)
    color[start] = 0
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if color[adj] == -1:
                color[adj] = 1 - color[node]
                q.append(adj)
            elif color[adj] == color[node]:
                return False
    return True

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            if not check(i, graph, color):
                return False
    return True
print(is_bipartite(graph))

