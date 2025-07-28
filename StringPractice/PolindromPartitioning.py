'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
'''
def checkPolindrom(ss):
    i=0
    j=len(ss)-1
    while i<j:
        if ss[i]!=ss[j]:
            return False
        i+=1
        j-=1
    return True

def PolindromPartitioning(s):
    def backtracking(start, path,res):
        if start==len(s):
            res.append(path[:])
            return
        for i in range(1, len(s)+1):
            if start+i>len(s):
                break
            seg=s[start:start+i]
            if checkPolindrom(seg):
                path.append(seg)
                backtracking(start+i, path, res)
                path.pop()
    path=[]
    res=[]
    backtracking(0, path, res)
    return res
s = "aab"
print(PolindromPartitioning(s))

    