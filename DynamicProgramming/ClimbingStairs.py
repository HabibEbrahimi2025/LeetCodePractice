def climbingStairs(n):
    if n<=2:
        return n    
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2

    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]





def climbStairs(n):
    res=[0]
    def backtracking(start, n):
        if start==n:
            res[0]+=1
            return
        if start>n:
            return
        
        for p in range(1,3):
            start+=p
            backtracking(start, n)
            start-=p
    backtracking(0, n)
    return res[0]
print(climbStairs(20))
print(climbingStairs(20))
        
