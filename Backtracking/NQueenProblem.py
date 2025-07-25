def nQueenProblem(n):

    def isSafe(board, row, col):
        for r,c in enumerate(board):
            if c==col:
                return False
            if abs(c-col) == abs(r-row):
                return False
        return True
    
    def backtracking(row, board, solution):
        if row==n:
            solution.append(board[:])
        
        for col in range(n):
            if isSafe(board, row, col):
                board.append(col)
                backtracking(row+1, board, solution)
                board.pop()
    
    solution=[]
    backtracking(0, [], solution)
    print(solution)
nQueenProblem(4)
    

