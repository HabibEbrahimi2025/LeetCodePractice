
'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

'''
from functools import lru_cache
def outOfBoundary(m, n, maxMove, startRow, startColumn):
    MOD = 10**9 + 7
    @lru_cache(None)
    def backtrack(i, j, movesLeft):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if movesLeft == 0:
            return 0
        total = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            total += backtrack(i + dx, j + dy, movesLeft - 1)
        return total % MOD

    return backtrack(startRow, startColumn, maxMove)      

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(outOfBoundary(m,n,maxMove, startRow, startColumn))

            
                