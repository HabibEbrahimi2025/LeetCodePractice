'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
'''
def combine(n, k):
    if n==0:
        return 0
    def backtracking(start, word, path, allPath):
        if len(path)==k:
            allPath.append(path[:])
            return
        for i in range(start, len(word)):
            path.append(word[i])
            backtracking(i+1, word, path, allPath)
            path.pop()
    word=[x for x in range(1,n+1)]
    allPath=[]
    backtracking(0, word, [], allPath)
    return allPath
n=1
k=1
combine(n,k)