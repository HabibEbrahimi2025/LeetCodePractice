def countDistinctSubsequnce(s):
    dp=[0]*(len(s)+1)
    last=dict()

    dp[0]=1
    for i in range(1, len(dp)):
        dp[i]=2*dp[i-1]

        ch=s[i-1]
        if ch in last:
            dp[i]-=dp[last[ch]-1]
        last[ch]=i
    print(dp[len(s)])

a="aacd"
countDistinctSubsequnce(a)