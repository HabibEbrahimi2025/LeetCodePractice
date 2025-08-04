def maxSubarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, arr[start:end+1]

# Example
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum, max_subarray = maxSubarray(arr)

# print("Maximum Subarray Sum:", max_sum)
# print("Maximum Subarray:", max_subarray)

def kadenAlg(arr):
    start=end=startApp=0
    totalSum=float('-inf')
    currentSum=0
    for i in range(len(arr)):
        currentSum+=arr[i]
        if currentSum>totalSum:
            totalSum=currentSum
            start=startApp
            end=i
        if currentSum<0:
            currentSum=0
            startApp=i+1
    return(totalSum, arr[start:end+1])

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadenAlg(arr))
