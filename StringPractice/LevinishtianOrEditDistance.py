'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''
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