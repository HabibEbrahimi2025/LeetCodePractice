'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
'''

def matrixSlidingWindow(matrix):

    def checkWindow(window):
        for i in range(len(window)):
            for j in range(len(window)):
                if window[i][j]!=1:
                    return False
        return True

    count=0
    pos=min(len(matrix), len(matrix[0]))
    w=1
    while w<=pos:
        row, col =len(matrix), len(matrix[0])
        for i in range(0,row-w+1):
            for j in range(0, col-w+1):
                window=[matrix[x][j:j+w] for x in range(i, i+w)]
                if checkWindow(window):
                    count+=1
        w+=1
    return count

def matrixSlidingWindowDP(matrix):
    if not matrix: return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0]*cols for _ in range(rows)]
    total = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1 
                else:
                    dp[i][j] = min(
                        dp[i-1][j],     
                        dp[i][j-1],     
                        dp[i-1][j-1]    
                    ) + 1
                total += dp[i][j]
    
    return total


matrix=[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

print(matrixSlidingWindowDP(matrix))

