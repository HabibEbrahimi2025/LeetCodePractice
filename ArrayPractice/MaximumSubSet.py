def findMaximumSubArray(start, arr, path, maxResult):
    currentSum=sum(path)
    if currentSum>maxResult[0]:
        maxResult[0]=currentSum
        maxResult[1]=path[:]
    print(path)
    for i in range(start, len(arr)):
        path.append(arr[i])
        findMaximumSubArray(i+1, arr, path, maxResult)
        path.pop()
allPath=[]
maxResult=[float('-inf'), []]
findMaximumSubArray(0, [-2,1,-3,4,-1,2,1,-5,4], [], maxResult)
print(maxResult[1])
print(maxResult[0])