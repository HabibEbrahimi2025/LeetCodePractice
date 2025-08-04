'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''
def findComb(candidates, target):
    def comb(start, candidates, target, path, allPath):
        if sum(path)==target:
            allPath.append(path[:])
            return
        
        if start>=len(candidates) or sum(path)>target:
            return
        
        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue

            path.append(candidates[i])
            comb(i+1, candidates, target, path, allPath)
            path.pop()

    candidates.sort()
    allPath=[]
    comb(0, candidates, target, [], allPath)
    return allPath

candidates = [10,1,2,7,6,1,5]
target=8
print(findComb(candidates, target))
