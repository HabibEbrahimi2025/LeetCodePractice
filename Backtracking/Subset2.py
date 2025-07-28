'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''
def generateSubset(nums):

    def backtracking(start, path, allPath):
        allPath.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtracking(i+1, path, allPath)
            path.pop()
    nums.sort()
    allPath=[]
    backtracking(0, [], allPath)
    newPth=[]
    for item in allPath:
        if item not in newPth:
            newPth.append(item[:])
    return newPth
nums = [0]
print(generateSubset(nums))