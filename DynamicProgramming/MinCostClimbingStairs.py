'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
'''
def minCostClimbingStiars(cost):
    n=len(cost)
    dp=[0]*(n+1)

    for i in range(2,n+1):
        dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[n]

cost = [10,15,20]
print(minCostClimbingStiars(cost))

    
