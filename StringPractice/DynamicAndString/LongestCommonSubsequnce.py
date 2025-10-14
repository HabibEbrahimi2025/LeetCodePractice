def longestCommonSubsequnce(s1,s2):
    dp=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]

    for i in range(1,len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j]=1+dp[i-1][j-1] if s2[i-1]==s1[j-1] else max(dp[i-1][j], dp[i][j-1])
    return dp[len(s2)][len(s1)]

s1="joha"
s2="john"
print(longestCommonSubsequnce(s1,s2))