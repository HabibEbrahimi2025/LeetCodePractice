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