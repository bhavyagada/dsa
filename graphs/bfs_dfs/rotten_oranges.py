from collections import deque
grid = [[2,1,1], [1,1,0], [0,1,1]]

def rotten_oranges(grid):
    # optimal => TC: O(nm), SC: O(nm)
    if grid is None or len(grid) == 0: return 0
    rows, cols = len(grid), len(grid[0])
    q = deque()
    count_fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count_fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    if count_fresh == 0: return 0

    count_time = 0
    while q and count_fresh > 0:
        count_time += 1
        for _ in range(len(q)):
            row, col = q.popleft()
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    count_fresh -= 1
    return count_time if count_fresh == 0 else -1
print(rotten_oranges(grid))
print(grid)

