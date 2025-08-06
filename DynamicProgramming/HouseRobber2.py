'''

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''
def houseRobber2(nums):
    n=len(nums)

    arr1=[nums[x] for x in range(n-1)]
    arr2=[nums[x] for x in range(1,n)]

    def houseRob(arr):
        dp=[0]*(len(arr))

        if len(arr)==1:
            return arr[0]
        if len(arr)==2:
            return max(arr[0], arr[1])
        dp[0]=arr[0]
        dp[1]=max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i]=max(dp[i-1], dp[i-2]+arr[i])
        return dp[len(arr)-1]
    res1=houseRob(arr1)
    res2=houseRob(arr2)

    return max(res1, res2)
nums=[1,2,3]
print(houseRobber2(nums))