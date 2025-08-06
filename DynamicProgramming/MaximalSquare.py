'''

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

'''
def maximalSquare(matrix):
    if not matrix:
        return 0
    
    row, col = len(matrix), len(matrix[0])
    dp=[[0]*col for _ in range(row)]

    maxValue=0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]=="1":
                if i==0 or j==0:
                    dp[i][j]=1
                    maxValue=max(maxValue, dp[i][j])
                else:
                    dp[i][j]=min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
                    maxValue=max(maxValue, dp[i][j])
    return maxValue*maxValue
matrix = [["0","1"],["1","0"]]
print(maximalSquare(matrix))
