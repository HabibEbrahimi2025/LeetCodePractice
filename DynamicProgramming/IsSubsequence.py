'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
'''
def isSubsequency(s, t):
    k=-1
    for i in range(len(s)):
        flag=False
        for j in range(k+1, len(t)):
            if s[i]==t[j]:
                flag=True
                k=j
                break
        if not flag:
            return False
    return True


def isSubsequence(s,t):
    m=len(s)
    n=len(t)

    dp=[[False] * (n+1) for _ in range(m+1)]

    for i in range(n+1):
        dp[0][i]=True
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=dp[i][j-1]
    return dp[m][n]


s="aaaaaa"
t="bbaaaa"

print(isSubsequence(s,t))

