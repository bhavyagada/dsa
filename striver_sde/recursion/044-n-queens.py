def solve(col, board, ans, leftrow, upper_diag, lower_diag, n):
    if col == n:
        ans.append(board.copy())
        return
    
    for row in range(n):
        if leftrow[row] == 0 and upper_diag[n-1+col-row] == 0 and lower_diag[row+col] == 0:
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            leftrow[row] = 1
            lower_diag[row+col] = 1
            upper_diag[n-1+col-row] = 1
            solve(col+1, board, ans, leftrow, upper_diag, lower_diag, n)
            upper_diag[n-1+col-row] = 0
            lower_diag[row+col] = 0
            leftrow[row] = 0
            board[row] = board[row][:col] + '.' + board[row][col+1:]

n = 4
board = ['.'*n for _ in range(n)]
leftrow = [0]*n
upper_diag = [0]*(2*n-1)
lower_diag = [0]*(2*n-1)
ans = []
solve(0, board, ans, leftrow, upper_diag, lower_diag, n)
print(ans)
