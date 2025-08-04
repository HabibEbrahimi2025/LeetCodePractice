'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''
def uniqueSubset(nums):
    def findAllSubset(start,nums, path, result):
        result.add(tuple(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            findAllSubset(i+1, nums, path, result)
            path.pop()
    path=[]
    result=set()
    findAllSubset(0, nums, path, result)
    nums2=[]
    for val in result:
        nums2.append(list(val))
    return nums2

nums = [1,2,3]
print(uniqueSubset(nums))

