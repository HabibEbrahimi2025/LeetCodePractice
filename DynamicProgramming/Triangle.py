'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
def findMinSum(triangle):
    k=0
    result=0
    result=triangle[0][0]
    for i in range(1,len(triangle)):
        if triangle[i][k]<triangle[i][k+1]:
            result+=triangle[i][k]
        else:
            result+=triangle[i][k+1]
            k+=1
    return result

triangle =[[-1],[2,3],[1,-1,-3]]


def miniMumTotal(triangle):
    dp=triangle[-1][:]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j]=triangle[i][j]+min(dp[j], dp[j+1])
    return dp[0]
print(miniMumTotal(triangle))

