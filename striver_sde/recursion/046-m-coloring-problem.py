def is_safe(node, col, edges, colors):
    for neighbor in edges[node]:
        if colors[neighbor] == col: return False
    return True

def color_edges(node, n, m, edges, colors):
    if node == n: return True
    
    for col in range(1, m+1):
        if is_safe(node, col, edges, colors):
            colors[node] = col
            if color_edges(node+1, n, m, edges, colors): return True
            colors[node] = 0
    return False

n = 4
edges = {0: [1,2], 1: [0,2], 2: [0,3], 3:[2]}
m = 3
colors = [0]*n
res = color_edges(0, n, m, edges, colors)
print(res)
assert res == True
