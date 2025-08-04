'''

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
'''

#Catalan number foumula
def catalanNumber(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        for j in range(i):
            dp[i]+=dp[j]*dp[i-1-j]
    return dp[n]
n=3
print(catalanNumber(n))