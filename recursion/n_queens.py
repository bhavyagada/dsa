n = 4

def queens(col, board, n, res, left_row, lower_diagonal, upper_diagnoal):
    # TC: O(n!), SC: O(n^2) + O(3n)
    if col == n:
        res.append(["".join(r) for r in board])
        return

    for row in range(n):
        if left_row[row] == 0 and lower_diagonal[row+col] == 0 and upper_diagnoal[n-1 + col-row] == 0:
            board[row][col] = "Q"
            left_row[row] = 1
            lower_diagonal[row+col] = 1
            upper_diagnoal[n-1 + col-row] = 1
            queens(col+1, board, n, res, left_row, lower_diagonal, upper_diagnoal)
            left_row[row] = 0
            lower_diagonal[row+col] = 0
            upper_diagnoal[n-1 + col-row] = 0
            board[row][col] = "."

res = []
board = [["." for _ in range(n)] for _ in range(n)]
left_row = [0] * n
lower_diagonal = [0] * (2*n-1)
upper_diagonal = [0] * (2*n-1)
queens(0, board, n, res, left_row, lower_diagonal, upper_diagonal)
print(res)

