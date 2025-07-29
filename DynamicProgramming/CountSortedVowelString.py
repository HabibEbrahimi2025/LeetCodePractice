'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
'''
def countSortedVowelString(n):
    if n==1:
        return 5
    dp=[[0]*6 for _ in range(n+1)]

    for i in range(6):
        dp[0][i]=1
    
    for i in range(1, n+1):
        for j in range(1, 6):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[n][5]

print(countSortedVowelString(33))

