def maximumProductSubArray(nums):
    finalResult=0
    currentSum=nums[0]
    for i in range(1,len(nums)):
        currentSum*=nums[i]
        finalResult=max(finalResult, currentSum)
        if currentSum<0:
            currentSum=0
    return finalResult

nums = [-2,0,-1]
print(maximumProductSubArray(nums))