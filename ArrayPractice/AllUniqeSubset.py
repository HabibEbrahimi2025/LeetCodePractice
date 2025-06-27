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

