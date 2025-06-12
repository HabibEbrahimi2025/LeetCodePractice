def editDistance(word1, word2):
    w1=len(word1)
    w2=len(word2)

    dp=[[0]*(w2+1) for _ in range(w1+1)]

    for i in range(w1+1):
        dp[i][0]=i
    for j in range(w2+1):
        dp[0][j]=j

    for i in range(1,w1+1):
        for j in range(1,w2+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(
                    dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )
    return dp[w1][w2]
word1="horse"
word2="ros"
print(editDistance(word1, word2))