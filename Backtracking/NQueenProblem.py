'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
'''
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
    

