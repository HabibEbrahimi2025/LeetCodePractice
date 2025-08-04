'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
def wordBreak(s, wordDict):
    def backtracking(subs):
        if len(subs)==0:
            return True
        
        for item in wordDict:
            if subs.find(item)==0:
                subs=subs[len(item):]
                if backtracking(subs):
                    return True
        return False
    return backtracking(s)

# s = "applepenapple"
# wordDict = ["apple","pen"]
# print(wordBreak(s, wordDict))

def wordBreak2(s, wordDict):
    memo={}
    def backtracking(start):
        if start==len(s):
            return True
        if start in memo:
            return memo[start]
        
        for end in range(start+1, len(s)+1):
            if s[start: start+end] in wordDict and backtracking(end):
                memo[start]=True
                return True
        memo[start]=False
        return False
    return backtracking(0)
s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa"]
print(wordBreak2(s, wordDict))