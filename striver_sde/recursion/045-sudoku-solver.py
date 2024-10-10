def solve_sudoku(board, rows, cols, squares):
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for n in range(1, 10):
                    if not rows[r][n] and not cols[c][n] and not squares[(r//3)*3+(c//3)][n]:
                        board[r][c] = str(n)
                        rows[r][n] = True
                        cols[c][n] = True
                        squares[(r//3)*3+(c//3)][n] = True
                        if solve_sudoku(board, rows, cols, squares): return True
                        else:
                            board[r][c] = "."
                            rows[r][n] = False
                            cols[c][n] = False
                            squares[(r//3)*3+(c//3)][n] = False
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
rows = [[False]*10 for _ in range(9)]
cols = [[False]*10 for _ in range(9)]
squares = [[False]*10 for _ in range(9)]
for r in range(9):
    for c in range(9):
        num = board[r][c]
        if num != ".":
            n = int(num)
            rows[r][n] = True
            cols[c][n] = True
            squares[(r//3)*3+(c//3)][n] = True
solve_sudoku(board, rows, cols, squares)
print(board)
assert board == [["5","3","4","6","7","8","9","1","2"],
                 ["6","7","2","1","9","5","3","4","8"],
                 ["1","9","8","3","4","2","5","6","7"],
                 ["8","5","9","7","6","1","4","2","3"],
                 ["4","2","6","8","5","3","7","9","1"],
                 ["7","1","3","9","2","4","8","5","6"],
                 ["9","6","1","5","3","7","2","8","4"],
                 ["2","8","7","4","1","9","6","3","5"],
                 ["3","4","5","2","8","6","1","7","9"]]
