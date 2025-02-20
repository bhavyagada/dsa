board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def solve(board, rows, cols, boxes):
    # TC: O(9^3), SC: O(3*9^2)
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for c in "123456789":
                    if c not in rows[row] and c not in cols[col] and c not in boxes[row//3][col//3]:
                        board[row][col] = c
                        rows[row].add(c)
                        cols[col].add(c)
                        boxes[row//3][col//3].add(c)
                        if solve(board, rows, cols, boxes): return True
                        board[row][col] = "."
                        rows[row].remove(c)
                        cols[col].remove(c)
                        boxes[row//3][col//3].remove(c)
                return False
    return True

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [[set() for _ in range(3)] for _ in range(3)]
for row in range(9):
    for col in range(9):
        if board[row][col] != ".":
            num = board[row][col]
            rows[row].add(num)
            cols[col].add(num)
            boxes[row//3][col//3].add(num)
solve(board, rows, cols, boxes)
print(board)


