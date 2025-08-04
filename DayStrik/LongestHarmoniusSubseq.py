def longestHarmouniousSubSeq(nums):
    nums.sort()
    finalLength=0
    j=0
    subArray=[]
    for i in range(len(nums)):
        subArray.append(nums[i])

        minV=min(subArray)
        maxV=max(subArray)

        if maxV-minV==1:
            finalLength=max(finalLength, len(subArray))
        elif maxV-minV>1:
            while maxV-minV!=1 and len(subArray)>1:
                subArray.remove(nums[j])
                j+=1
                maxV=max(subArray)
                minV=min(subArray)
    print(finalLength)
nums = [1,3,2,2,5,2,3,7]
longestHarmouniousSubSeq(nums)



