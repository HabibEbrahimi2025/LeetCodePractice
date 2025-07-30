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
