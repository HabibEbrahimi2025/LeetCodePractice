def longestCommonSubString(s1,s2):
    dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]


    holdMax=0
    x=0
    y=0
    for i in range(1, len(dp)):
        for  j in range(1, len(dp[0])):
            dp[i][j]=dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else 0

            if dp[i][j]>holdMax:
                holdMax=dp[i][j]
                x=i
                y=j
    print(holdMax)
    print(x,",",y)

s1="Alikhan"
s2="khanAlijan"
longestCommonSubString(s1,s2)