def maximumDifference(nums):
    res=-1

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):

            if i<j and  nums[i]<nums[j]:
                r=nums[j]-nums[i]
                if r>res:
                    res=r
    return res
nums = [7,1,5,4]
print(maximumDifference(nums)) 