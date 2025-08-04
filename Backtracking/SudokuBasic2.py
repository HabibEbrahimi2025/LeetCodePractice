def solveSudoku(board):
    def isValid(board, row, col, num):
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check 3x3 box
        boxRowStart = (row // 3) * 3
        boxColStart = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[boxRowStart + i][boxColStart + j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Empty cell
                    for num in range(1, 10):
                        if isValid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = 0  # Backtrack
                    return False  # No valid number found
        return True  # All cells filled

    if backtrack():
        print("Sudoku Solved:")
        for row in board:
            print(row)
    else:
        print("No solution exists.")

# Example Input (0 represents empty cells)
board = [
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0]
]

solveSudoku(board)
