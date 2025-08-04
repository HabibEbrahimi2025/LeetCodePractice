def houseRobber(nums):

    n=len(nums)

    dp=[0]*n

    if not nums:
        return 0
    if n==1:
        return nums[0]
    if n==2:
        return max(nums[0], nums[1])
    
    dp[0]=nums[0]
    dp[1]=max(nums[0], nums[1])
    for i in range(2, n):
        dp[i]=max(dp[i-1], dp[i-2]+nums[i])
    return dp[n-1]

    
nums = [2,7,9,3,1]
print(houseRobber(nums))