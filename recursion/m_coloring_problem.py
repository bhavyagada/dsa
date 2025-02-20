from collections import defaultdict

v = 4
edges = [(0,1),(1,2),(2,3),(3,0),(0,2)]
m = 3

def can_color(node, graph, node_colors, c):
    for adj in graph[node]:
        if node_colors[adj] == c: return False
    return True

def color(node, v, m, graph, node_colors):
    # TC: O(n^m), SC: O(n) + O(n)
    if node == v: return True

    for c in range(1, m+1):
        if can_color(node, graph, node_colors, c):
            node_colors[node] = c
            if color(node+1, v, m, graph, node_colors): return True
            node_colors[node] = 0
    return False

node_colors = [0] * v
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
print(color(0, v, m, graph, node_colors))

