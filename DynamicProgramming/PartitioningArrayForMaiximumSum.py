'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
'''
def partitioningArray(arr, k):
    n=len(arr)
    dp=[0]*(n+1)

    for i in range(1, n+1):
        maxSum=0
        for length in range(1, min(k, i)+1):
            maxSum=max(maxSum, arr[i-length])
            dp[i]=max(dp[i], dp[i-length]+maxSum*length)
    return dp[i]

arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4
print(partitioningArray(arr, k))
