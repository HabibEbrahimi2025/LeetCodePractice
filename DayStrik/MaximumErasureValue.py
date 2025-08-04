def maximumErasureValue(nums):
    maxValue=float('-inf')
    seen=set()
    left=0
    currentSum=0
    
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            currentSum-=nums[left]
            left+=1
        seen.add(nums[right])
        currentSum+=nums[right]
        maxValue=max(maxValue, currentSum)
    print(maxValue)

nums = [5,2,1,2,5,2,1,2,5]
maximumErasureValue(nums)